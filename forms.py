from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    {% extends "layout.html" %}
    {% block content %}
        <div class="content-section">
            <form method="POST" action="">
            {{ form.hidden_tag() }}
            <fieldset class="form-group">
             <div class="form-group">
     {{ form.username.label(class="form-control-label") }}
     {% if form.username.errors %}
       {{ form.username(class="form-control form-control-lg is-invalid") }}
       <div class="invalid-feedback">
         {% for error in form.username.errors%}
             <span>{{error}}</span>
         {% endfor %}
       </div>
   {% else %}
       {{ form.username(class="form-control form-control-lg") }}
   {% endif %}
 </div>
 {% if form.username.errors %}
        {{ form.username(class="form-control form-control-lg is-invalid") }}
        <div class="invalid-feedback">
          {% for error in form.username.errors%}
              <span>{{error}}</span>
          {% endfor %}
        </div>
