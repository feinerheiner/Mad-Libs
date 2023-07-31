from django.db import models


# Create your models here.
class Story(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    content = models.TextField()


class Input(models.Model):
    def __str__(self):
        return self.input_name

    TYPES = (
        ('noun1', 'Noun1'),
        ('noun2', 'Noun2'),
        ('noun3', 'Noun3'),
        ('noun4', 'Noun4'),
        ('noun5', 'Noun5'),
        ('noun6', 'Noun6'),
        ('noun7', 'Noun7'),
        ('noun8', 'Noun8'),
        ('noun9', 'Noun9'),
        ('noun10', 'Noun10'),
        ('verb1', 'Verb1'),
        ('verb2', 'Verb2'),
        ('verb3', 'Verb3'),
        ('verb4', 'Verb4'),
        ('verb5', 'Verb5'),
        ('verb6', 'Verb6'),
        ('verb7', 'Verb7'),
        ('verb8', 'Verb8'),
        ('verb9', 'Verb9'),
        ('verb10', 'Verb10'),
        ('adjective1', 'Adjective1'),
        ('adjective2', 'Adjective2'),
        ('adjective3', 'Adjective3'),
        ('adjective4', 'Adjective4'),
        ('adjective5', 'Adjective5'),
        ('adjective6', 'Adjective6'),
        ('adjective7', 'Adjective7'),
        ('adjective8', 'Adjective8'),
        ('adjective9', 'Adjective9'),
        ('adjective10', 'Adjective10'),
        ('adverb1', 'Adverb1'),
        ('animal1', 'Animal1'),
        ('animal2', 'Animal2'),
        ('animal3', 'Animal3'),
        ('food1', 'Food1'),
        ('food2', 'Food2'),
        ('food3', 'Food3'),
        ('previous noun', 'Previous Noun'),
        ('location1', 'Location1'),
        ('location2', 'Location2'),
        ('location3', 'Location3'),
        ('game1', 'Game1'),
        ('plural noun1', 'Plural Noun1'),
        ('plural noun2', 'Plural Noun2'),
        ('verb ending in -ing', 'Verb Ending in -ing'),
        ('verb ending in -ing2', 'Verb Ending in -ing2'),
        ('verb ending in -ed1', 'Verb Ending in -ed1'),
        ('first noun', 'First Noun'),
        ('first food', 'First Food'),
        ('person1', 'Person1'),
        ('person2', 'Person2'),
        ('person3', 'Person3'),
        ('adverb1', 'Adverb1'),
        ('occupation1', 'Occupation1'),
        ('relation1', 'Relation1'),
        ('body part1', 'Body part1'),
        ('number1', 'Number1'),
        ('number2', 'Number2'),
        ('occupation2', 'Occupation2'),
        ('relation1', 'Relation1'),
        ('body part', 'Body part'),
        ('liquid1', 'Liquid1'),
        ('color1', 'Color1'),
        ('government position', 'Government position'),
        ('holiday', 'Holiday'),
        ('crime1', 'Crime1'),
        ('name1', 'Name1'),
    )
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    input_name = models.CharField(max_length=40, choices=TYPES)
    order = models.IntegerField()


class UserInput(models.Model):
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

