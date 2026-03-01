from django import forms
from .models import ContactInquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-white dark:bg-gray-800/50 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-3 text-slate-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:border-primary-500 focus:ring-1 focus:ring-primary-500 focus:outline-none transition-colors',
                'placeholder': 'Your Full Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-white dark:bg-gray-800/50 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-3 text-slate-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:border-primary-500 focus:ring-1 focus:ring-primary-500 focus:outline-none transition-colors',
                'placeholder': 'your@email.com',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full bg-white dark:bg-gray-800/50 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-3 text-slate-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:border-primary-500 focus:ring-1 focus:ring-primary-500 focus:outline-none transition-colors',
                'placeholder': '+233 XX XXX XXXX',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full bg-white dark:bg-gray-800/50 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-3 text-slate-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:border-primary-500 focus:ring-1 focus:ring-primary-500 focus:outline-none transition-colors',
                'placeholder': 'What can we help you with?',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-white dark:bg-gray-800/50 border border-gray-300 dark:border-gray-700 rounded-lg px-4 py-3 text-slate-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:border-primary-500 focus:ring-1 focus:ring-primary-500 focus:outline-none transition-colors resize-none',
                'placeholder': 'Tell us about your project...',
                'rows': 5,
            }),
        }
