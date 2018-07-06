from django.shortcuts import render, redirect
from .models import Image, Title, MenuItem, Button, ShowcaseText, SectionAText, SectionBText, SectionCCard, SectionDText
from django.contrib.auth import authenticate, login
from django.views.generic import View
from home.forms import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import get_template



def index(request) :
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)
        send_mail('New contact submission',
                  content,
                  contact_email,
                  ['shane.m.calhoun@gmail.com'], fail_silently=False)

        # email = EmailMessage(
        #     "New contact form submission",
        #     content,
        #     contact_name,
        #     ['shane.m.calhoun@gmail.com'],
        #     headers={'Reply-To': contact_email}
        # )
        # email.send()
        return redirect('index')

    context = {
        #images
        "showcaseImg": Image.objects.get(title="showcase_img"),
        "arrow": Image.objects.get(title="showcase_arrow"),
        "a1": Image.objects.get(title="sectionA_img1"),
        "a2": Image.objects.get(title="sectionA_img2"),
        "a3": Image.objects.get(title="sectionA_img3"),
        "affiliate1": Image.objects.get(title="affiliates1"),
        "affiliate2": Image.objects.get(title="affiliates2"),
        "affiliate3": Image.objects.get(title="affiliates3"),

        #titles
        "homePage_title": Title.objects.get(title="homePage_title"),
        "showcase_title": Title.objects.get(title="showcase_title"),
        "sectionA_title": Title.objects.get(title="sectionA_title"),
        "sectionB_title": Title.objects.get(title="sectionB_title"),
        "sectionC_title": Title.objects.get(title="sectionC_title"),
        "affiliates_title": Title.objects.get(title="affiliates_title"),
        "contact_title": Title.objects.get(title="contact_title"),

        #MenuItems
        "menuItem1": MenuItem.objects.get(title="menuItem1"),
        "menuItem2": MenuItem.objects.get(title="menuItem2"),
        "menuItem3": MenuItem.objects.get(title="menuItem3"),
        "menuItem4": MenuItem.objects.get(title="menuItem4"),
        # "menuItem5": MenuItem.objects.get(title="menuItem5"),
        "menuItem6": MenuItem.objects.get(title="menuItem6"),

        #buttons
        "showcase_btn1": Button.objects.get(title="showcase_btn1"),
        "showcase_btn2": Button.objects.get(title="showcase_btn2"),
        "sectionA_btn1": Button.objects.get(title="sectionA_btn1"),
        "sectionC_btn1": Button.objects.get(title="sectionC_btn1"),
        "sectionB_btn1": Button.objects.get(title="sectionB_btn1"),
        "sectionB_btn2": Button.objects.get(title="sectionB_btn2"),
        "sectionD_btn1": Button.objects.get(title="sectionD_btn1"),
        "arrow_btn": Button.objects.get(title="arrow_btn"),

        #showcase text
        "overview1": ShowcaseText.objects.get(title="overview1"),
        "overview2": ShowcaseText.objects.get(title="overview2"),
        "overview3": ShowcaseText.objects.get(title="overview3"),
        "overview_black": ShowcaseText.objects.get(title="overview_black"),
        "credentials_name": ShowcaseText.objects.get(title="credentials_name"),
        "credentials_certifications": ShowcaseText.objects.get(title="credentials_certifications"),
        "credentials_trade": ShowcaseText.objects.get(title="credentials_trade"),

        #section A text
        "about": SectionAText.objects.get(title="about"),
        "sectionA_more_content": SectionAText.objects.get(title="more_content"),

        #section B text
        "blog_subscribe_text": SectionBText.objects.get(title="blog_subscribe_text"),

        #section C cards
        "cards": SectionCCard.objects.all(),

        #section D text
        "contact_prompt": SectionDText.objects.get(title="contact_prompt"),
        "copyRight": SectionDText.objects.get(title="copyRight"),

        "form": form_class,

    }

    return render(request, 'home/index.html', context)

