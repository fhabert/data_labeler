from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from labeler.models import Person
from labeler.forms import PersonRegister, PersonLogin, Answer
from django.contrib.auth import authenticate, login, get_user_model
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from tensorflow.keras.models import load_model

import pandas as pd
import numpy as np
from PIL import Image
import base64

# Need an external dataset access
DATASET_CV = pd.read_csv("D:/dataset_data_labeler/computer_vision/mnist_train.csv")
DATASET_RE = "D:/dataset_data_labeler/real_estate/contrat_immo.png"
DATASET_L = "D:/dataset_data_labeler/law/contrat_law.jpg"
INDEX = 0

class HomeView(TemplateView):
    template_name ="home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        return context
        
class RegisterView(TemplateView):
    template_name = "register.html"
    
    def get(self, request):
        form = PersonRegister()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = PersonRegister(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            likes_law = form.cleaned_data.get("likes_law")
            likes_real_estate = form.cleaned_data.get("likes_real_estate")
            likes_computer_vision = form.cleaned_data.get("likes_computer_vision")
            password = form.cleaned_data.get("password")
            user = Person.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, \
                                          likes_law=likes_law, likes_real_estate=likes_real_estate, likes_computer_vision=likes_computer_vision, \
                                            password=make_password(password))
            login(request, user)
            return redirect("/user/{}/".format(user.username))
        return render(request, "register.html", {'form': form})
    

class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        form = PersonLogin()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    # request.session['user'] = username
                    return redirect("/user/{}/".format(user.username))
                else:
                    error_message = "Invalid email or password.."
                    return render(request, "login.html", {'error_message': error_message})
            except Person.DoesNotExist:
                return render(request, "login.html")
        return render(request, "login.html")
    

class UserView(TemplateView):
    template_name = "user.html"

    def get(self, request, username):
        global INDEX
        user = Person.objects.get(username=username)
        if request.user.is_authenticated:      
        # login(request, user)
            interests = self.get_interests(user)
            context = { "username": user.username, "interests": interests }
            if user.first_connexion:
                image_data = self.img_to_b64(Image.fromarray(np.array(DATASET_CV.iloc[INDEX, 1:], dtype=np.uint8).reshape((28,28))))
                INDEX += 1
                form = Answer()
                context["image_data"] = image_data
                context["form"] = form 
                if INDEX == 2:
                    context["completed"] = True
                    context["rate_success"] = user.rate_success
                    user.first_connexion = False
                    user.save()
            else:
                if user.likes_computer_vision:
                    image_data = self.img_to_b64(Image.fromarray(np.array(DATASET_CV.iloc[0, 1:], dtype=np.uint8).reshape((28,28))))
                elif user.likes_law:
                    image_data = self.img_to_b64(Image.fromarray(np.array(Image.open(DATASET_L).resize((28,28)), dtype=np.int8)))
                elif user.likes_real_estate:
                    print("HELLOOOO")
                    image_data = self.img_to_b64(Image.fromarray(np.array(Image.open(DATASET_RE).resize((1024,1024)), dtype=np.int8)))
                form = Answer()
                context["image_data"] = image_data
                context["form"] = form
        return render(request, "user.html", context )
    
    def img_to_b64(self, img):
        image_bytes = BytesIO()
        img.save(image_bytes, format='PNG')
        image_bytes.seek(0)
        image_data = image_bytes.getvalue()
        image_data = base64.b64encode(image_data).decode("utf-8")
        return image_data
    
    def get_interests(self, user):
        interests = []
        if user.likes_computer_vision:
            interests.append("Computer Vision")
        if user.likes_law: 
            interests.append("Law")
        if user.likes_real_estate:
            interests.append("Real Estate")
        return interests
    
    def post(self, request, username):
        if request.method == "POST":
            form = Answer(request.POST)
            if form.is_valid():
                current_user = request.user
                response = np.int64(form.cleaned_data.get('answer'))
                pixels = form.cleaned_data.get('pixels')
                nlp_model = load_model("nlp_model.h5")
                image_bytes = base64.b64decode(pixels)
                image = Image.open(BytesIO(image_bytes))
                array_pix = np.array(image).reshape((-1,28,28,1))
                prediction = nlp_model.predict(array_pix)
                predicted_class = np.argmax(prediction)
                current_user.total_answers += 1
                if predicted_class == response:
                    current_user.good_answers += 1
                    current_user.save()
                    context = { "username": current_user.username }
                else:
                    current_user.save()
                    context = { "username": current_user.username }
            return redirect("/user/{}/".format(current_user.username), context)
        return render(request, "user.html")