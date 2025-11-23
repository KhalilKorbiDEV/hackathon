"""
Data generator for fake news detection training
Creates sample dataset for demonstration purposes
"""

import csv
import random
from datetime import datetime, timedelta

def generate_sample_data(filename='data/fake_news_data.csv', num_samples=1000):
    """Generate sample fake news dataset"""
    
    fake_titles = [
        "Breaking: Secret government conspiracy exposed",
        "Scientists discover miracle cure hidden by Big Pharma",
        "New study shows vaccines cause autism",
        "Celebrity reveals shocking truth about illuminati",
        "Aliens spotted near major cities worldwide",
        "Historic discovery: Ancient pyramids built by aliens",
        "Shocking video proves flat earth theory",
        "5G towers cause COVID-19 pandemic",
        "Hollywood stars part of secret pedophile ring",
        "Water fluoridation is mind control",
        "Moon landing was fake, NASA admits",
        "Reptilians control world governments",
    ]
    
    real_titles = [
        "New AI breakthrough improves healthcare diagnostics",
        "Stock market reaches all-time high",
        "Scientists develop renewable energy solution",
        "University research shows climate change impact",
        "Tech company announces new product line",
        "Global GDP growth expected this quarter",
        "Medical team completes successful surgery",
        "New infrastructure project begins construction",
        "Education reform bill passes parliament",
        "International trade agreement reaches agreement",
        "Space agency launches new satellite mission",
        "Public health initiative proves effective",
    ]
    
    fake_content = [
        "According to anonymous sources, the government has been hiding the truth",
        "Multiple conspiracy theories suggest...",
        "Unverified reports claim that...",
        "Alleged leaked documents show...",
        "Common rumors suggest...",
        "Based on speculation and hearsay...",
        "Internet claims that...",
        "Social media posts indicate...",
    ]
    
    real_content = [
        "According to peer-reviewed research published in...",
        "Official government records show that...",
        "Scientific studies conducted by universities demonstrate...",
        "Published data from credible sources indicates...",
        "Documented facts show that...",
        "Verified reports from news agencies confirm...",
        "Official statistics compiled by authorities show...",
        "Research institutions worldwide have confirmed...",
    ]
    
    sources_fake = ["RedditTruth", "ConspiracyDaily", "AlternativeNews", "TruthBombs", "HiddenReality"]
    sources_real = ["Reuters", "BBC", "AP News", "The Guardian", "NPR", "Bloomberg", "CNN"]
    
    data = []
    
    # Generate real news
    for i in range(num_samples // 2):
        date = datetime.now() - timedelta(days=random.randint(0, 365))
        data.append({
            'title': random.choice(real_titles),
            'content': random.choice(real_content),
            'source': random.choice(sources_real),
            'date': date.strftime("%Y-%m-%d"),
            'label': 'real'
        })
    
    # Generate fake news
    for i in range(num_samples // 2):
        date = datetime.now() - timedelta(days=random.randint(0, 365))
        data.append({
            'title': random.choice(fake_titles),
            'content': random.choice(fake_content),
            'source': random.choice(sources_fake),
            'date': date.strftime("%Y-%m-%d"),
            'label': 'fake'
        })
    
    # Write to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'content', 'source', 'date', 'label'])
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Generated {len(data)} samples in {filename}")
    return filename

if __name__ == "__main__":
    generate_sample_data()
