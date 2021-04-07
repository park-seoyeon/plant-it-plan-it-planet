from django.db import models


class FilterChild(models.Model):
    id = models.IntegerField(primary_key=True)
    property_id = models.IntegerField()
    child_property_id = models.CharField(max_length=100)
    parents_property_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter_child'


class FilterProperty(models.Model):
    id = models.IntegerField(primary_key=True)
    property = models.CharField(max_length=45)
    property_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'filter_property'


class PlantFilter(models.Model):
    id = models.IntegerField(primary_key=True)
    plant_name = models.CharField(max_length=45)
    leafy = models.IntegerField(db_column='Leafy')  # Field name made lowercase.
    hanging = models.IntegerField(db_column='Hanging')  # Field name made lowercase.
    cactus_succulent = models.IntegerField(db_column='Cactus_Succulent')  # Field name made lowercase.
    vine = models.IntegerField(db_column='Vine')  # Field name made lowercase.
    fragrant = models.IntegerField(db_column='Fragrant')  # Field name made lowercase.
    has_flower = models.IntegerField(db_column='Has_flower')  # Field name made lowercase.
    has_fruit = models.IntegerField(db_column='Has_fruit')  # Field name made lowercase.
    without_leaves = models.IntegerField(db_column='Without_leaves')  # Field name made lowercase.
    wooden = models.IntegerField(db_column='Wooden')  # Field name made lowercase.
    chubby = models.IntegerField(db_column='Chubby')  # Field name made lowercase.
    no_soil = models.IntegerField(db_column='No_soil')  # Field name made lowercase.
    no_spike_cactus = models.IntegerField(db_column='No_spike_cactus')  # Field name made lowercase.
    holed = models.IntegerField(db_column='Holed')  # Field name made lowercase.
    broad = models.IntegerField(db_column='Broad')  # Field name made lowercase.
    round = models.IntegerField(db_column='Round')  # Field name made lowercase.
    sharp = models.IntegerField(db_column='Sharp')  # Field name made lowercase.
    long = models.IntegerField(db_column='Long')  # Field name made lowercase.
    split = models.IntegerField(db_column='Split')  # Field name made lowercase.
    heart_shaped = models.IntegerField(db_column='Heart_shaped')  # Field name made lowercase.
    star_shaped = models.IntegerField(db_column='Star_shaped')  # Field name made lowercase.
    small = models.IntegerField(db_column='Small')  # Field name made lowercase.
    thick = models.IntegerField(db_column='Thick')  # Field name made lowercase.
    patterned = models.IntegerField(db_column='Patterned')  # Field name made lowercase.
    flower_shaped = models.IntegerField(db_column='Flower_shaped')  # Field name made lowercase.
    fat = models.IntegerField(db_column='Fat')  # Field name made lowercase.
    flat = models.IntegerField(db_column='Flat')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant_filter'


