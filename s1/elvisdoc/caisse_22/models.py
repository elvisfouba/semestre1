from django.db import models

# Create your models here.
class etudiants(models.Model):
        nom = models.CharField('Nom', max_length=100)
        prenom= models.CharField('Prenom', max_length=100)
        sexe= models.CharField('Sexe', max_length=30)
        filiere= models.CharField('Filière', max_length=100)
        niveau= models.CharField('Niveau', max_length=30)
        statut= models.CharField('Statut',max_length=30)
        num_matricule= models.CharField('Num_matricule', max_length=30)

        def __str__(self):
         return self.prenom 
            
class payements(models.Model):
        date_payement = models.DateField('Date_payement', max_length= 100)
        description = models.CharField('Description', max_length= 100)
        montant = models.IntegerField('Montant')
        avance = models.IntegerField('Avance',max_length=200)
        reste = models.IntegerField ('Reste')
        rendez_vous = models.DateField('Rendez_vous',max_length= 120)
        etudiants = models.ForeignKey(etudiants,blank=False, null=False, on_delete=models.CASCADE)

    
        def __str__(self):
         return self.description

class Caissier(models.Model):
        nom = models.CharField('Nom', max_length=100)
        adresse = models.CharField('Adresse', max_length=100)
        email = models.CharField('Email', max_length=100)
    
        def __str__(self):
         return self.nom



class Enregistrements (models.Model):
        ref_enregist = models.CharField('Ref_enregistrement', max_length= 120)
        date_enregist = models.DateTimeField('Date_enregistrement',max_length=200)
        auteur = models.CharField('Auteur', max_length= 120)
        payements = models.ForeignKey(payements,blank=False, null=False, on_delete=models.CASCADE)
        caissier = models.ForeignKey(Caissier, blank=False, null=False, on_delete=models.CASCADE)

        def __str__(self):
         return self.ref_enregist




class caisses (models.Model):
        ref_caisses = models.CharField('Ref_caisses', max_length= 100)
        montant = models.IntegerField('Montant',max_length=100)
        statut = models.CharField('Statut', max_length= 100)
        commentaire = models.CharField('Commentaire', max_length= 200)
        caisiers = models.ForeignKey(Caissier,blank=False, null=False, on_delete=models.CASCADE)
        
        def __str__(self):
         return self.montant

  