from django import forms


class IntegerChoiceField(forms.ChoiceField):
    def to_python(self, value):
        if value in self.empty_values:
            return None
        return int(value)
    

# Create your models here.
class LoveTester(forms.Form):

    def __str__(self):
       return "models of form in love tester feature"


    CHOICES_RACE = (
        (1,'Black/African American'),
        (2,'European/Caucasian-American'),
        (3,'Latino/Hispanic American'),
        (4,'Asian/Pacific Islander/Asian-American'),
        (5,'Native American'),
        (6,'Other')
    )
    
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
    ]

    MET_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    FREQUENCY_CHOICES = (
        (1, 'Several times a week'),
        (2, 'Twice a week'),
        (3, 'Once a week'),
        (4, 'Twice a month'),
        (5, 'Once a month'),
        (6, 'Several times a year'),
        (7, 'Almost never')
    )

    CAREER_CHOICES = (
        (1, 'Lawyer'),
        (2, 'Academic/Research'),
        (3, 'Psychologist'),
        (4, 'Doctor/Medicine'),
        (5, 'Engineer'),
        (6, 'Creative Arts/Entertainment'),
        (7, 'Banking/Consulting/Finance/Marketing/Business/CEO/Entrepreneur/Admin'),
        (8, 'Real Estate'),
        (9, 'International/Humanitarian Affairs'),
        (10, 'Undecided'),
        (11, 'Social Work'),
        (12, 'Speech Pathology'),
        (13, 'Politics'),
        (14, 'Pro sports/Athletics'),
        (15, 'Other'),
        (16, 'Journalism'),
        (17, 'Architecture')
    )


    FIELDS_OF_STUDY = [(1, 'Law'), (2, 'Math'), (3, 'Social Science, Psychologist'), (4, 'Medical Science, Pharmaceuticals, and Bio Tech'), (5, 'Engineering'), (6, 'English/Creative Writing/Journalism'), (7, 'History/Religion/Philosophy'), (8, 'Business/Econ/Finance'), (9, 'Education, Academia'), (10, 'Biological Sciences/Chemistry/Physics'), (11, 'Social Work'), (12, 'Undergrad/undecided'), (13, 'Political Science/International Affairs'), (14, 'Film'), (15, 'Fine Arts/Arts Administration'), (16, 'Languages'), (17, 'Architecture'), (18, 'Other')]
    
    RANGE_CHOICES = [x for x in zip(range(1, 11), range(1, 11))]

    gender = IntegerChoiceField(choices=GENDER_CHOICES, label="user gender")

    race_o = IntegerChoiceField(choices=CHOICES_RACE, label="race of user partner")
    age_o = forms.IntegerField(label="age of user partner")
    pf_o_sin = IntegerChoiceField(choices=RANGE_CHOICES, label="user prefer of sincere")
    pf_o_int = IntegerChoiceField(choices=RANGE_CHOICES, label="user prefer of intelligent")
    pf_o_fun = IntegerChoiceField(choices=RANGE_CHOICES, label="user prefer of fun")
    pf_o_amb = IntegerChoiceField(choices=RANGE_CHOICES, label="user prefer of ambitious")
    pf_o_sha = IntegerChoiceField(choices=RANGE_CHOICES, label="user prefer of shared interests")

    sinc_o = IntegerChoiceField(choices=RANGE_CHOICES, label="rate of sincere partner by user")
    intel_o = IntegerChoiceField(choices=RANGE_CHOICES, label="rate of intelligent partner by user")
    fun_o = IntegerChoiceField(choices=RANGE_CHOICES, label="rate of fun partner by user")
    amb_o = IntegerChoiceField(choices=RANGE_CHOICES, label="rate of ambitious partner by user")
    shar_o = IntegerChoiceField(choices=RANGE_CHOICES, label="rate of shared interests partner by user")
    like_o = IntegerChoiceField(choices=RANGE_CHOICES, label="Overall, how much do you like this person?(1=don't like at all, 10=like a lot)")
    prob_o = IntegerChoiceField(choices=RANGE_CHOICES, label="How probable do you think it is that this person will say 'yes' for you?(1=not probable, 10=extremely probable)")
    met_o = IntegerChoiceField(choices=MET_CHOICES, label="Have you met this person before?")
    
    age = forms.IntegerField(label="user age")
    
    field_cd = IntegerChoiceField(choices=FIELDS_OF_STUDY, label="user field of study")
    race = IntegerChoiceField(choices=CHOICES_RACE, label="user race")
    imprace = IntegerChoiceField(choices=RANGE_CHOICES, label="How important is it to you (on a scale of 1-10) that a person you date be of the same racial/ethnic background?")
    imprelig = IntegerChoiceField(choices=RANGE_CHOICES, label="How important is it to you (on a scale of 1-10) that a person you date be of the same religious background?")
    income = forms.IntegerField(label="user income ($)")
    date = IntegerChoiceField(choices=FREQUENCY_CHOICES, label="In general, how frequently do you go on dates?")
    go_out = IntegerChoiceField(choices=FREQUENCY_CHOICES, label="In general, how frequently do you go for hangout?")
    career_c = IntegerChoiceField(choices=CAREER_CHOICES, label="What is your intended career?")
    sports = IntegerChoiceField(choices=RANGE_CHOICES, label="in the scale 1-10 for sport interest?")
    tvsports = IntegerChoiceField(choices=RANGE_CHOICES, label="in the scale 1-10 for watching tv interest?")
    exercise = IntegerChoiceField(choices=RANGE_CHOICES, label="in the scale 1-10 for exercise interest?")
    dining = IntegerChoiceField(choices=RANGE_CHOICES, label="in the scale 1-10 for dining interest?")
    museums = IntegerChoiceField(choices=RANGE_CHOICES, label="in the scale 1-10 for museums interest?")
   

