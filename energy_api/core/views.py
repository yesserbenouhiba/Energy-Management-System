from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db import connection

class SocieteViewSet(viewsets.ModelViewSet):
    queryset = Societe.objects.all()
    serializer_class = SocieteSerializer

class CompteViewSet(viewsets.ModelViewSet):
    queryset = Compte.objects.all()
    serializer_class = CompteSerializer

class CompteurElecViewSet(viewsets.ModelViewSet):
    queryset = CompteurElec.objects.all()
    serializer_class = CompteurElecSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['societe__id']

class CompteurGazViewSet(viewsets.ModelViewSet):
    queryset = CompteurGaz.objects.all()
    serializer_class = CompteurGazSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['societe__id']

class DemandeCotationViewSet(viewsets.ModelViewSet):
    queryset = DemandeCotation.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['type', 'status']

    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return DemandeCotationReadSerializer
        return DemandeCotationWriteSerializer

class VenteProViewSet(viewsets.ModelViewSet):
    queryset = VentePro.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['fournisseur', 'status']

    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return VenteProReadSerializer
        return VenteProWriteSerializer


#Showing key metrics (active contracts, pending quotations)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_metrics(request):
    active_contracts_count = VentePro.objects.filter(status='Active').count()
    pending_quotations_count = DemandeCotation.objects.filter(status='Pending').count()
    
    data = {
        'active_contracts': active_contracts_count,
        'pending_quotations': pending_quotations_count,
    }
    return Response(data)

#List all quotation requests with company and account details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def quotation_requests_with_details(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                dc.id,
                dc.type,
                dc.status,
                dc.numCompteur,
                s.nom AS company_name,
                s.siret,
                s.siren,
                s.email AS company_email,
                c.nom AS account_lastname,
                c.prenom AS account_firstname,
                c.email AS account_email,
                c.type AS account_type
            FROM 
                core_demandecotation dc
            JOIN 
                core_societe s ON dc.societe_id = s.id
            JOIN 
                core_compte c ON dc.compte_id = c.id;
        """)
        results = dict_fetchall(cursor)
    return Response(results)

#Sales statistics grouped by energy type and company
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sales_statistics(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                s.nom AS company_name,
                vp.fournisseur,
                COUNT(*) AS total_sales,
                CASE 
                    WHEN vp.numCompteur IN (SELECT numCompteur FROM core_compteurelec) THEN 'ELEC'
                    WHEN vp.numCompteur IN (SELECT numCompteur FROM core_compteurgaz) THEN 'GAZ'
                    ELSE 'UNKNOWN'
                END AS energy_type
            FROM 
                core_ventepro vp
            JOIN 
                core_societe s ON vp.societe_id = s.id
            GROUP BY 
                s.nom, vp.fournisseur, energy_type;
        """)
        results = dict_fetchall(cursor)
    return Response(results)

#Average contract duration by supplier
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def average_contract_duration(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                fournisseur,
                AVG(JULIANDAY(dateFinFourniture) - JULIANDAY(dateDebutFourniture)) AS average_duration_days
            FROM 
                core_ventepro
            WHERE 
                status = 'Active'
            GROUP BY 
                fournisseur;
        """)
        results = dict_fetchall(cursor)
    return Response(results)

#Helper function to convert cursor results to dictionaries
def dict_fetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

