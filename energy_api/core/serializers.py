from rest_framework import serializers
from .models import *

class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = '__all__'

class CompteurElecSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteurElec
        fields = '__all__'

class CompteurGazSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteurGaz
        fields = '__all__'

class SocieteSerializer(serializers.ModelSerializer):
    compteurelec_set = CompteurElecSerializer(many=True, read_only=True)
    compteurgaz_set = CompteurGazSerializer(many=True, read_only=True)

    class Meta:
        model = Societe
        fields = '__all__'

# Serializer for GET (read) with nested serializers
class DemandeCotationReadSerializer(serializers.ModelSerializer):
    societe = SocieteSerializer(read_only=True)
    compte = CompteSerializer(read_only=True)

    class Meta:
        model = DemandeCotation
        fields = '__all__'

# Serializer for POST/PUT/PATCH (write) with IDs only
class DemandeCotationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeCotation
        fields = '__all__'

# Serializer for GET (read) with nested serializers
class VenteProReadSerializer(serializers.ModelSerializer):
    societe = SocieteSerializer(read_only=True)

    class Meta:
        model = VentePro
        fields = '__all__'

# Serializer for POST/PUT/PATCH (write) with IDs only
class VenteProWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentePro
        fields = '__all__'
