from django import forms

class MyForm(forms.Form):
    CHOICES = (
        ('opcion1', 'Mañana'),
        ('opcion2', 'Noche'),
        ('opcion3', 'Sabatina'),
        ('opcion4', 'Tarde'),
        ('opcion5', 'Única'),
    )
    dropdown1 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}), label='Jornada del colegio')

    CHOICES_2 = (
        ('opcion6', 'Oficial'),
        ('opcion7', 'Privado'),
    )
    dropdown2 = forms.ChoiceField(choices=CHOICES_2, widget=forms.Select(attrs={'class': 'form-control'}),label='Naturaleza del colegio')

    CHOICES_3 = (
        ('opcion8', 'Femenino'),
        ('opcion9', 'Masculino'),
        ('opcion10','Mixto'),
    )
    dropdown3 = forms.ChoiceField(choices=CHOICES_3, widget=forms.Select(attrs={'class': 'form-control'}),label='Género del colegio')

    CHOICES_4 = (
        ('opcion11', 'Rural'),
        ('opcion12', 'Urbano'),
    )
    dropdown4 = forms.ChoiceField(choices=CHOICES_4, widget=forms.Select(attrs={'class': 'form-control'}),label='Ubicación del colegio')

    CHOICES_5 = (
        ('opcion13', 'Antioquia'),
        ('opcion14', 'Arauca'),
        ('opcion15', 'Atlántico'),
        ('opcion16', 'Bogotá'),
        ('opcion17', 'Bolivar'),
        ('opcion18', 'Boyacá'),
        ('opcion19', 'Caldas'),
        ('opcion20', 'Caqueta'),
        ('opcion21', 'Casanare'),
        ('opcion22', 'Cauca'),
        ('opcion23', 'Cesar'),
        ('opcion24', 'Choco'),
        ('opcion25', 'Cordoba'),
        ('opcion26', 'Cundinamarca'),
        ('opcion27', 'Guainia'),
        ('opcion28', 'Guaviare'),
        ('opcion29', 'Huila'),
        ('opcion30', 'la Guajira'),
        ('opcion31', 'Magdalena'),
        ('opcion32', 'Meta'),
        ('opcion33', 'Nariño'),
        ('opcion34', 'Norte de Santander'),
        ('opcion35', 'Putumayo'),
        ('opcion36', 'Quindio'),
        ('opcion37', 'Risaralda'),
        ('opcion38', 'San Andrés'),
        ('opcion39', 'Santander'),
        ('opcion40', 'Sucre'),
        ('opcion41', 'Tolima'),
        ('opcion42', 'Valle'),
        ('opcion43', 'Vaupés'),
        ('opcion44', 'Vichada'),
    )
    dropdown5 = forms.ChoiceField(choices=CHOICES_5, widget=forms.Select(attrs={'class': 'form-control'}),label='Departamento del colegio')

    CHOICES_6 = (
        ('opcion45', 'No trabajo'),
        ('opcion46', 'Menos de 10 horas'),
        ('opcion47', 'Entre 11 y 20 horas'),
        ('opcion48', 'Entre 21 y 30 horas'),
        ('opcion49', 'Más de 30 horas'),
    )
    dropdown6 = forms.ChoiceField(choices=CHOICES_6, widget=forms.Select(attrs={'class': 'form-control'}), label='Número de horas que el estudiante trabaja laboralmente a la semana')

    CHOICES_7 = (
        ('opcion50', 'No leo ni por entretenimiento'),
        ('opcion51', 'Menos de una hora'),
        ('opcion52', 'Entre una y dos horas'),
        ('opcion53', 'Más de dos horas'),

    )
    dropdown7 = forms.ChoiceField(choices=CHOICES_7, widget=forms.Select(attrs={'class': 'form-control'}), label='Número de horas que el estudiante dedica a la lectura diaria (Sin contar el colegio)')

    CHOICES_8 = (
        ('opcion54', 'Mejor'),
        ('opcion55', 'Peor'),
    )
    dropdown8 = forms.ChoiceField(choices=CHOICES_8, widget=forms.Select(attrs={'class': 'form-control'}),label='Situación económica de la familia después de la pandemia')

    CHOICES_9 = (
        ('opcion56', 'Nunca o rara vez comemos eso'),
        ('opcion57', 'Tres o cinco veces por semana'),
        ('opcion58', 'Todos o casi todos los días'),
    )
    dropdown9 = forms.ChoiceField(choices=CHOICES_9, widget=forms.Select(attrs={'class': 'form-control'}), label='Número de veces que la familia come carne, huevo, pollo o pescado a la semana')

    CHOICES_10 = (
        ('opcion59', 'De uno a diez libros'),
        ('opcion60', 'De once a veinticinco libros'),
        ('opcion61', 'De veintiseis a cien libros'),
        ('opcion62', 'Más de cien libros'),
    )
    dropdown10 = forms.ChoiceField(choices=CHOICES_10, widget=forms.Select(attrs={'class': 'form-control'}), label='Número de libros en el hogar')

    CHOICES_11 = (
        ('opcion63', 'Sí'),
        ('opcion64', 'No'),

    )
    dropdown11 = forms.ChoiceField(choices=CHOICES_11, widget=forms.Select(attrs={'class': 'form-control'}),label='Tiene computador en el hogar')

    CHOICES_12 = (
        ('opcion65', 'Sí'),
        ('opcion66', 'No'),

    )
    dropdown12 = forms.ChoiceField(choices=CHOICES_12, widget=forms.Select(attrs={'class': 'form-control'}), label='Tiene internet en el hogar')

    CHOICES_13 = (
        ('opcion67', 'Ninguno'),
        ('opcion68', 'No sabe'),
        ('opcion69', 'No aplica'),
        ('opcion70', 'Primaria incompleta'),
        ('opcion71', 'Primaria completa '),
        ('opcion72', 'Secundaria incompleta'),
        ('opcion73', 'Secundaria completa'),
        ('opcion74', 'Técnica o tecnológica incompleta '),
        ('opcion75', 'Técnica o tecnológica completa '),
        ('opcion76', 'Educación profesional incompleta'),
        ('opcion77', 'Educación profesional completa'),
        ('opcion78', 'Posgrado'),


    )
    dropdown13 = forms.ChoiceField(choices=CHOICES_13, widget=forms.Select(attrs={'class': 'form-control'}),label='Nivel educativo de la mamá')

    CHOICES_14 = (
        ('opcion79', 'Ninguno'),
        ('opcion80', 'No sabe'),
        ('opcion81', 'No aplica'),
        ('opcion82', 'Primaria incompleta'),
        ('opcion83', 'Primaria completa '),
        ('opcion84', 'Secundaria incompleta'),
        ('opcion85', 'Secundaria completa'),
        ('opcion86', 'Técnica o tecnológica incompleta '),
        ('opcion87', 'Técnica o tecnológica completa '),
        ('opcion88', 'Educación profesional incompleta'),
        ('opcion89', 'Educación profesional completa'),
        ('opcion90', 'Posgrado'),

    )
    dropdown14 = forms.ChoiceField(choices=CHOICES_14, widget=forms.Select(attrs={'class': 'form-control'}), label='Nivel educativo del papá')
