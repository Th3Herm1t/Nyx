# mbti_app/views.py

from django.shortcuts import render, redirect
from ..models import UserInput
from ..forms import MBTIForm

# views.py
from django.shortcuts import render
import joblib
from django.views.decorators.csrf import csrf_protect
import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

@csrf_protect
def home(request):
    form = MBTIForm()

    if request.method == 'POST':
        form = MBTIForm(request.POST)
        print(form.errors)
    if form.is_valid():
        user_input_text = form.cleaned_data['text']

        # Perform prediction using the SVM model
        predicted_mbti, personality_description = predict_mbti(user_input_text)

        # Pass the predicted result and personality description to the template for rendering
        return render(request, 'home.html', {'form': form, 'predicted_mbti': predicted_mbti, 'personality_description': personality_description})

    return render(request, 'home.html', {'form': form})


def tokenize_and_clean_with_progress(text):
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stop words
    tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens

# Load the label encoder
label_encoder = joblib.load('/workspaces/Nyx/label_encoder.joblib')

def tokenize_and_clean_with_progress(text):
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stop words
    tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens

PERSONALITY_PROFILES = {
    'ISTJ': 'The Inspector - ISTJs are responsible organizers, driven to create and enforce order within systems and institutions.',
    'ISFJ': 'The Protector - ISFJs are industrious caretakers, loyal to traditions and organizations. They are practical, compassionate, and caring.',
    'INFJ': 'The Counselor - INFJs are creative nurturers with a strong sense of idealism and integrity. They are insightful and considerate of others.',
    'INTJ': 'The Mastermind - INTJs are strategic thinkers, motivated to organize change. They are independent, analytical, and decisive.',
    'ISTP': 'The Craftsman - ISTPs are observant, adventurous doers. They are practical and realistic, with a keen eye for details.',
    'ISFP': 'The Composer - ISFPs are gentle caretakers with a strong appreciation for beauty. They are kind, sensitive, and artistic.',
    'INFP': 'The Healer - INFPs are empathetic idealists, dedicated to pursuing their dreams and creating a positive impact on the world.',
    'INTP': 'The Architect - INTPs are innovative thinkers, fascinated by the logical order of the world. They are open-minded and curious.',
    'ESTP': 'The Dynamo - ESTPs are energetic thrill-seekers who are spontaneous and enthusiastic. They are pragmatic and adaptable.',
    'ESFP': 'The Performer - ESFPs are vivacious entertainers who love life and people. They are outgoing, fun-loving, and spontaneous.',
    'ENFP': 'The Champion - ENFPs are enthusiastic and creative individuals with a passion for exploring possibilities and connecting with others.',
    'ENTP': 'The Visionary - ENTPs are resourceful and creative thinkers who enjoy solving complex problems. They are witty and adaptable.',
    'ESTJ': 'The Supervisor - ESTJs are dedicated organizers, committed to maintaining order and enforcing rules within their environment.',
    'ESFJ': 'The Provider - ESFJs are conscientious caregivers who are generous and dependable. They are social, nurturing, and responsible.',
    'ENFJ': 'The Teacher - ENFJs are compassionate leaders, driven by a strong sense of empathy and a desire to help others.',
    'ENTJ': 'The Commander - ENTJs are strategic leaders, motivated to organize people and resources to achieve their vision. They are assertive and decisive.'
}

def predict_mbti(text):
    # Load the TF-IDF vectorizer and SVM model
    vectorizer = joblib.load('/workspaces/Nyx/vectorizer.joblib')
    svm_model = joblib.load('/workspaces/Nyx/svm_model1.pkl')
    
    tokens = tokenize_and_clean_with_progress(text)

    # Transform the input text using the vectorizer
    text_vectorized = vectorizer.transform([' '.join(tokens)])

    # Make predictions using the SVM model
    predicted_mbti = svm_model.predict(text_vectorized)[0]
   # Load the label encoder
    label_encoder = joblib.load('/workspaces/Nyx/label_encoder.joblib')
    original_label = label_encoder.inverse_transform([predicted_mbti])[0]

    # Fetch personality description from the dictionary
    personality_description = PERSONALITY_PROFILES.get(original_label)

    return original_label, personality_description


