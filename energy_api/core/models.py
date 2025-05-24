from django.db import models
from django.contrib.auth.models import User

class Societe(models.Model):
    nom = models.CharField(max_length=100)
    siret = models.CharField(max_length=14)
    siren = models.CharField(max_length=9)
    adressePostal = models.TextField()
    codePostal = models.CharField(max_length=10)
    commune = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Compte(models.Model):
    TYPE_CHOICES = [('Admin', 'Admin'), ('Commercial', 'Commercial'), ('Client', 'Client')]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    email = models.EmailField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.type})" 


class CompteurElec(models.Model):
    numCompteur = models.CharField(max_length=50)
    adresseCompteur = models.CharField(max_length=255)
    optionTarifaire = models.CharField(max_length=100)
    puissance = models.IntegerField()
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Elec Meter {self.numCompteur} - {self.societe.nom}"


class CompteurGaz(models.Model):
    numCompteur = models.CharField(max_length=50)
    adresseCompteur = models.CharField(max_length=255)
    consommation = models.DecimalField(max_digits=10, decimal_places=2)
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Gaz Meter {self.numCompteur} - {self.societe.nom}"


class DemandeCotation(models.Model):
    TYPE_CHOICES = [('GAZ', 'GAZ'), ('ELEC', 'ELEC')]
    STATUS_CHOICES = [('Pending', 'Pending'), ('Validated', 'Validated')]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    numCompteur = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.type} Cotation for {self.societe.nom} - {self.status}"


class VentePro(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('Active', 'Active'), ('Cancelled', 'Cancelled')]
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)
    fournisseur = models.CharField(max_length=100)
    numCompteur = models.CharField(max_length=50)
    dateDebutFourniture = models.DateField()
    dateFinFourniture = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Vente {self.fournisseur} ({self.status}) for {self.societe.nom}"