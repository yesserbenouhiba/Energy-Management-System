from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'societes', SocieteViewSet)
router.register(r'comptes', CompteViewSet)
router.register(r'compteurs-elec', CompteurElecViewSet)
router.register(r'compteurs-gaz', CompteurGazViewSet)
router.register(r'demandes-cotation', DemandeCotationViewSet)
router.register(r'ventepro', VenteProViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # URL for dashboard metrics: shows key figures like active contracts and pending quotations
    path('dashboard-metrics/', dashboard_metrics, name='dashboard-metrics'),
    # URLs providing various statistics endpoints:
    # - /stats/quotations/ : Lists all quotation requests with detailed company and account info
    # - /stats/sales/ : Shows sales statistics grouped by energy type and company
    # - /stats/average-duration/ : Calculates average duration of active contracts by supplier
    path('stats/quotations/', quotation_requests_with_details, name='quotation-details'),
    path('stats/sales/', sales_statistics, name='sales-statistics'),
    path('stats/average-duration/', average_contract_duration, name='average-contract-duration'),
]
