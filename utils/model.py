from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Career dataset (VERY IMPORTANT)
careers = {
    "Data Scientist": "python machine learning data analysis statistics",
    "Web Developer": "html css javascript frontend backend react",
    "AI Engineer": "python deep learning neural networks tensorflow",
    "Cyber Security": "network security ethical hacking cryptography",
    "Software Engineer": "java c++ problem solving algorithms"
}

# Convert text into numbers
vectorizer = TfidfVectorizer()

# Train on career data
career_texts = list(careers.values())
career_vectors = vectorizer.fit_transform(career_texts)


def predict_career(user_input):
    # Convert user input into vector
    user_vector = vectorizer.transform([user_input])

    # Compare with all careers
    similarity = cosine_similarity(user_vector, career_vectors)

    # Get best match
    index = similarity.argmax()

    # Get career name
    career_name = list(careers.keys())[index]

    # Confidence score
    score = float(similarity[0][index])

    return career_name, score
