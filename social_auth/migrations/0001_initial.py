# Generated by Django 5.0.1 on 2024-02-21 01:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_sessions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_question', models.TextField()),
                ('question_received_timestamp', models.DateTimeField(auto_now_add=True)),
                ('bot_response', models.TextField()),
                ('response_sent_timestamp', models.DateTimeField()),
                ('rating', models.IntegerField(choices=[(0, 'Sin calificar'), (1, 'Baja calidad'), (2, 'Regular'), (3, 'Buena'), (4, 'Muy buena'), (5, 'Excelente')], default=0, help_text='Calificación de la respuesta del chatbot en una escala de 1 a 5.')),
                ('feedback', models.TextField(blank=True, help_text='Comentarios adicionales sobre la respuesta del chatbot. Máximo 500 caracteres.', max_length=500, null=True)),
                ('chat_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='social_auth.chatsession')),
            ],
        ),
    ]
