from django import forms


class EditarDatosForm(forms.Form):
    
    nombre_usuario = forms.CharField(
        label='Nombre de Usuario Nuevo',
        widget=forms.TextInput,
        required=True
    )
    
    email = forms.EmailField(
        label='Nuevo Email',
        widget=forms.EmailInput,
        required=True
    )



class EditarContraseñaForm(forms.Form):
    
    password = forms.CharField(
        label='Contraseña actual', 
        widget=forms.PasswordInput,
        required=True
    )
    new_password = forms.CharField(
        label='Nueva contraseña', 
        widget=forms.PasswordInput,
        required=True
    )
    repeat_password = forms.CharField(
        label='Repetir nueva contraseña', 
        widget=forms.PasswordInput,
        required=True
    )
    
    
    def clean(self):
        datos_limpios = super().clean()
        new_password = datos_limpios.get('new_password')
        repeat_password = datos_limpios.get('repeat_password')

        if new_password != repeat_password:
            self.add_error('Las contraseñas no coinciden.')
