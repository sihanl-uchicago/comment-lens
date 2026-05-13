import streamlit as st

st.set_page_config(
    page_title="CommentLens",
    page_icon="🔍",
    layout="wide"
)

# -----------------------------
# Query Classification
# -----------------------------
def classify_query(query):
    q = query.lower()

    if any(k in q for k in ["咖啡", "coffee", "cafe", "brunch", "餐厅", "restaurant", "甜品", "dessert"]):
        return "Food & Places"
    if any(k in q for k in ["杭州", "上海", "北京", "东京", "旅行", "旅游", "trip", "travel", "hotel"]):
        return "Travel"
    if any(k in q for k in ["面霜", "护肤", "口红", "防晒", "敏感肌", "skincare", "makeup", "beauty"]):
        return "Beauty"
    if any(k in q for k in ["lululemon", "aritzia", "穿搭", "衣服", "包", "fashion", "outfit"]):
        return "Fashion"
    if any(k in q for k in ["mba", "留学", "申请", "大学", "graduate", "school"]):
        return "Education"
    if any(k in q for k in ["ai", "chatgpt", "app", "软件", "产品", "tech"]):
        return "Tech"

    return "Lifestyle"


# -----------------------------
# Recommendation Mode Database
# -----------------------------
def get_recommendations(query):
    q = query.lower()

    # Chicago coffee shops
    if ("芝加哥" in q or "chicago" in q) and ("咖啡" in q or "coffee" in q or "cafe" in q):
        return {
            "mode": "Recommendation Mode",
            "title": "Chicago Coffee Shop Recommendations",
            "summary": "CommentLens detected that this is a location-based recommendation query. Instead of giving a general category summary, it ranks specific places based on simulated social-comment patterns, including what users like, what they complain about, and how reliable the signal appears.",
            "items": [
                {
                    "name": "Sawada Coffee",
                    "score": 88,
                    "sentiment": "Positive",
                    "why": "Frequently mentioned for matcha latte, industrial-style space, and strong photo appeal.",
                    "best_for": "First-time visitors, photo lovers, friend catch-ups",
                    "watch_out": "Can be crowded during weekends; seating may be limited.",
                    "comment_pattern": "Most positive comments mention atmosphere and matcha drinks, while negative comments focus on crowding and wait time.",
                    "quotes": [
                        "“The matcha latte is the reason I would come back.”",
                        "“Great vibe, but I would not go during peak weekend hours.”"
                    ]
                },
                {
                    "name": "The Wormhole Coffee",
                    "score": 84,
                    "sentiment": "Positive",
                    "why": "Loved for its retro theme, cozy neighborhood feel, and distinctive Wicker Park identity.",
                    "best_for": "Solo work, vintage lovers, relaxed weekend visits",
                    "watch_out": "Small space; may not be ideal for large groups.",
                    "comment_pattern": "Users often describe it as more memorable than standard coffee chains, but less convenient for long seating.",
                    "quotes": [
                        "“The vibe is more special than a regular coffee shop.”",
                        "“Cute place, but seats fill up quickly.”"
                    ]
                },
                {
                    "name": "La Colombe",
                    "score": 79,
                    "sentiment": "Stable",
                    "why": "Seen as a reliable and convenient option with consistent coffee quality.",
                    "best_for": "Quick coffee runs, studying, low-risk choices",
                    "watch_out": "Less unique compared with independent local cafes.",
                    "comment_pattern": "Comments are consistent but less emotionally enthusiastic; users value reliability more than novelty.",
                    "quotes": [
                        "“Reliable coffee when I do not want to take risks.”",
                        "“Good quality, but not the most memorable cafe.”"
                    ]
                },
                {
                    "name": "Intelligentsia Coffee",
                    "score": 81,
                    "sentiment": "Positive",
                    "why": "Recognized for coffee quality and specialty coffee reputation.",
                    "best_for": "Coffee enthusiasts, work breaks, people who care about beans and taste",
                    "watch_out": "Some users find it less cozy and more functional.",
                    "comment_pattern": "Positive comments emphasize coffee quality; weaker comments mention limited atmosphere.",
                    "quotes": [
                        "“The coffee itself is strong and reliable.”",
                        "“Good for coffee, not necessarily for a long hangout.”"
                    ]
                }
            ]
        }

    # Hangzhou food / cafes / travel
    if "杭州" in q and any(k in q for k in ["咖啡", "餐厅", "美食", "brunch", "cafe", "food"]):
        return {
            "mode": "Recommendation Mode",
            "title": "Hangzhou Food & Cafe Recommendations",
            "summary": "This query combines a city and a consumer decision need. CommentLens therefore switches into recommendation mode and highlights specific types of places users are likely looking for.",
            "items": [
                {
                    "name": "West Lake Area Cafes",
                    "score": 86,
                    "sentiment": "Positive",
                    "why": "Highly discussed for scenery, walkability, and photo-friendly cafe experiences.",
                    "best_for": "Tourists, couples, slow weekend trips",
                    "watch_out": "Crowded during holidays; some places may feel overpriced.",
                    "comment_pattern": "Users praise scenery and atmosphere but complain about holiday crowds.",
                    "quotes": [
                        "“The view is beautiful, but avoid national holidays.”",
                        "“Good for photos and slow walks.”"
                    ]
                },
                {
                    "name": "Wulin / Kerry Centre Restaurants",
                    "score": 80,
                    "sentiment": "Stable",
                    "why": "Mentioned as convenient, central, and suitable for visitors who want lower-risk dining.",
                    "best_for": "First-time visitors, groups, people who want convenience",
                    "watch_out": "Less local and less surprising than hidden neighborhood spots.",
                    "comment_pattern": "Comments emphasize convenience more than uniqueness.",
                    "quotes": [
                        "“Easy choice when you do not want to plan too much.”",
                        "“Convenient, but not the most local experience.”"
                    ]
                },
                {
                    "name": "Local Noodle & Small Eats Shops",
                    "score": 83,
                    "sentiment": "Positive",
                    "why": "Often praised for local flavor and better value compared with tourist-area restaurants.",
                    "best_for": "Foodies, budget travelers, local-experience seekers",
                    "watch_out": "Environment may be simple; not always photo-friendly.",
                    "comment_pattern": "Positive comments focus on taste and value; complaints focus on environment.",
                    "quotes": [
                        "“Small local places are more worth it than tourist restaurants.”",
                        "“Not fancy, but the taste feels more authentic.”"
                    ]
                }
            ]
        }

    return None


# -----------------------------
# Insight Mode Generator
# -----------------------------
def generate_insights(query, category):
    base = {
        "Food & Places": {
            "sentiment": (69, 20, 11),
            "confidence": 76,
            "confidence_reason": "Medium-high confidence: food and place-related comments usually contain clear signals such as taste, price, location, atmosphere, and waiting time. However, without live API access, this MVP uses representative patterns rather than real-time comments.",
            "summary": f"Discussions around {query} are generally positive, but users make decisions based on specific trade-offs: taste, atmosphere, price, waiting time, and whether the place is worth a dedicated visit.",
            "likes": [
                "Users respond strongly to atmosphere, visual appeal, and social-sharing value.",
                "Positive comments usually mention taste, convenience, or suitability for friend gatherings.",
                "Posts with specific menu items or visit scenarios tend to feel more trustworthy."
            ],
            "complaints": [
                "Waiting time and crowding are recurring pain points.",
                "Some users question whether the experience justifies the price.",
                "Experience can vary by location, timing, and user expectations."
            ],
            "themes": ["Taste", "Atmosphere", "Price-value", "Waiting time", "Photo appeal"],
            "decision_signal": "Worth trying if the user cares about atmosphere and social experience, but should check recent comments for crowding and price-value.",
            "risk_signals": [
                "General search terms may mix very different user intents.",
                "Viral posts may overrepresent visually attractive but average places.",
                "Comments may be biased by time of visit or neighborhood."
            ],
            "recommendations": [
                "Search with a more specific intent, such as 'best for studying', 'date spot', or 'worth the line'.",
                "Compare positive comments with negative comments before deciding.",
                "Prioritize recent comments over old viral posts."
            ],
            "quotes": [
                f"“{query} looks good, but I would check whether it is worth the wait.”",
                f"“The vibe matters as much as the food itself.”",
                f"“Good for photos, but price-value depends on what you order.”"
            ],
            "persona": "Best for foodies, social explorers, friend gatherings, and users who care about atmosphere."
        },
        "Travel": {
            "sentiment": (72, 18, 10),
            "confidence": 82,
            "confidence_reason": "High confidence: travel comments tend to cluster around clear dimensions such as scenery, itinerary difficulty, crowding, transportation, and cost.",
            "summary": f"Discussions around {query} are positive but practical. Users are interested in whether the destination is beautiful, easy to plan, worth the cost, and suitable for their travel style.",
            "likes": [
                "Scenic spots and photo-friendly experiences are frequently praised.",
                "Users value local food, cafes, and short-trip potential.",
                "Many comments frame the topic as suitable for weekend or holiday planning."
            ],
            "complaints": [
                "Crowds during holidays are the most common complaint.",
                "Transportation and itinerary planning can be tiring.",
                "Some popular spots are described as over-commercialized."
            ],
            "themes": ["Scenery", "Crowds", "Transportation", "Food", "Itinerary planning"],
            "decision_signal": "Worth considering if the user avoids peak periods and plans around specific neighborhoods or experiences.",
            "risk_signals": [
                "Travel comments are highly seasonal.",
                "Viral posts may make destinations look easier or prettier than reality.",
                "Different traveler types may have opposite opinions."
            ],
            "recommendations": [
                "Filter by travel length, such as one-day trip, weekend trip, or family trip.",
                "Check complaints about crowding and transportation before making plans.",
                "Look for posts from users with similar travel style."
            ],
            "quotes": [
                f"“{query} is beautiful, but avoid peak season.”",
                f"“Planning ahead makes the experience much better.”",
                f"“The hidden local spots are more interesting than the famous ones.”"
            ],
            "persona": "Best for weekend travelers, couples, foodies, and photo lovers."
        },
        "Beauty": {
            "sentiment": (64, 22, 14),
            "confidence": 74,
            "confidence_reason": "Medium confidence: beauty comments contain useful signals, but results vary heavily by skin type, routine, climate, and expectation.",
            "summary": f"Discussions around {query} are mixed-positive. Users care about texture, visible results, skin compatibility, price, and whether the product is worth repurchasing.",
            "likes": [
                "Texture, packaging, and ease of daily use are frequently mentioned.",
                "Users value gradual but visible improvement.",
                "Repeat purchase intention appears when price feels reasonable."
            ],
            "complaints": [
                "Effectiveness varies by skin type.",
                "Price sensitivity is high.",
                "Some users say results require consistent use."
            ],
            "themes": ["Skin type", "Texture", "Repurchase", "Price", "Visible results"],
            "decision_signal": "Potentially worth trying, but only if the user matches the skin type and use case mentioned in positive comments.",
            "risk_signals": [
                "Individual skin reactions can differ significantly.",
                "Sponsored or viral content may distort perceived effectiveness.",
                "Short-term reviews may not reflect long-term results."
            ],
            "recommendations": [
                "Look for comments from users with the same skin type.",
                "Separate texture reviews from actual effectiveness reviews.",
                "Check negative comments for irritation, breakouts, or poor value."
            ],
            "quotes": [
                f"“{query} feels nice, but it is not a miracle product.”",
                f"“I would repurchase if there is a discount.”",
                f"“It worked for me, but skin type really matters.”"
            ],
            "persona": "Best for skincare beginners, sensitive-skin users, and value-conscious buyers."
        },
        "Fashion": {
            "sentiment": (67, 21, 12),
            "confidence": 78,
            "confidence_reason": "Medium-high confidence: fashion comments often contain concrete signals around sizing, fit, styling, price, and durability.",
            "summary": f"Discussions around {query} are positive when users see strong design and styling value, but hesitation appears around sizing, durability, and price-performance.",
            "likes": [
                "Design, fit, and daily wearability are frequently mentioned.",
                "Brand image creates strong purchase interest.",
                "Users like items that are easy to style."
            ],
            "complaints": [
                "Sizing can be inconsistent.",
                "Price is a major concern.",
                "Some users question durability or cost-performance."
            ],
            "themes": ["Fit", "Sizing", "Daily styling", "Brand value", "Durability"],
            "decision_signal": "Worth considering if the user values brand, style, and daily wearability more than pure cost-performance.",
            "risk_signals": [
                "Sizing feedback may differ by body type.",
                "Viral styling posts may not reflect long-term durability.",
                "Discount timing can strongly affect purchase sentiment."
            ],
            "recommendations": [
                "Search for size-specific reviews before buying.",
                "Check comments on fabric and durability.",
                "Compare full-price sentiment versus sale-price sentiment."
            ],
            "quotes": [
                f"“{query} looks good, but size selection matters.”",
                f"“I like the style, but I waited for a sale.”",
                f"“Very wearable for daily outfits.”"
            ],
            "persona": "Best for young professionals, lifestyle shoppers, and trend followers."
        },
        "Education": {
            "sentiment": (61, 27, 12),
            "confidence": 71,
            "confidence_reason": "Medium confidence: education-related comments are useful but highly dependent on background, goals, budget, and career path.",
            "summary": f"Discussions around {query} focus on outcomes, cost, application stress, peer experience, and whether the investment is worth it.",
            "likes": [
                "Users care most about outcomes, career value, and peer experience.",
                "Practical application advice receives strong engagement.",
                "First-hand experience is considered more trustworthy than generic guides."
            ],
            "complaints": [
                "Cost and uncertainty are major concerns.",
                "The application process feels stressful.",
                "Information quality varies significantly across posts."
            ],
            "themes": ["Career value", "Cost", "Peer experience", "Application strategy", "Uncertainty"],
            "decision_signal": "Worth exploring if the user has a clear goal and can compare outcomes across similar backgrounds.",
            "risk_signals": [
                "Advice may not transfer across countries, schools, or career paths.",
                "Success stories may be overrepresented.",
                "Older posts may be outdated."
            ],
            "recommendations": [
                "Prioritize comments from users with similar background.",
                "Separate emotional reassurance from actionable advice.",
                "Check whether advice is recent and program-specific."
            ],
            "quotes": [
                f"“{query} is valuable, but you need to be clear about your goal.”",
                f"“The most useful posts are from people who actually went through it.”",
                f"“Cost is the biggest thing to consider.”"
            ],
            "persona": "Best for applicants, career switchers, and international students."
        },
        "Tech": {
            "sentiment": (66, 24, 10),
            "confidence": 73,
            "confidence_reason": "Medium confidence: tech comments reveal adoption interest and pain points, but user understanding varies widely.",
            "summary": f"Discussions around {query} show curiosity and early adoption interest, but users still care about setup difficulty, trust, examples, and whether the tool fits real workflows.",
            "likes": [
                "Users are curious about productivity gains and practical use cases.",
                "Early adopters share detailed workflows.",
                "Clear tutorials and examples increase trust."
            ],
            "complaints": [
                "Some users are confused about setup.",
                "Trust and accuracy concerns remain.",
                "Users want more examples before paying."
            ],
            "themes": ["Use cases", "Onboarding", "Trust", "Productivity", "Willingness to pay"],
            "decision_signal": "Strong interest exists, but adoption depends on clear workflow examples and low-friction onboarding.",
            "risk_signals": [
                "Some users may misunderstand the product capability.",
                "Hype can inflate expectations.",
                "Free versus paid user sentiment may differ."
            ],
            "recommendations": [
                "Highlight specific use cases instead of generic benefits.",
                "Add onboarding examples or templates.",
                "Use trust signals such as limitations and accuracy notes."
            ],
            "quotes": [
                f"“{query} is useful once you know the right workflow.”",
                f"“The idea is cool, but onboarding could be better.”",
                f"“I want more examples before paying for it.”"
            ],
            "persona": "Best for students, creators, productivity users, and early adopters."
        },
        "Lifestyle": {
            "sentiment": (58, 29, 13),
            "confidence": 65,
            "confidence_reason": "Medium-low confidence: broad lifestyle queries often mix multiple intents, so the signal is useful but less precise.",
            "summary": f"Discussions around {query} are broad and subjective. Users show curiosity, but comments may reflect different needs, contexts, and personal preferences.",
            "likes": [
                "Users show broad curiosity and emotional engagement.",
                "Many posts focus on personal experience and decision-making.",
                "The topic is useful for discovering trends and consumer pain points."
            ],
            "complaints": [
                "Comments are scattered and subjective.",
                "General searches need stronger filtering.",
                "Users often disagree depending on personal preference."
            ],
            "themes": ["Personal preference", "Trend discovery", "Emotional reaction", "Use case differences"],
            "decision_signal": "Useful for trend exploration, but the user should refine the query for a stronger recommendation.",
            "risk_signals": [
                "Search intent is broad.",
                "Comments may reflect very different user groups.",
                "Viral posts may dominate the perceived sentiment."
            ],
            "recommendations": [
                "Narrow the query by city, product type, use case, or budget.",
                "Compare multiple comment clusters instead of relying on one summary.",
                "Use negative comments to identify decision risks."
            ],
            "quotes": [
                f"“{query} has mixed reviews, so I checked multiple posts.”",
                f"“The comments are more useful than the post itself.”",
                f"“It depends a lot on personal preference.”"
            ],
            "persona": "Best for trend explorers, casual researchers, and consumer insight users."
        }
    }

    return base.get(category, base["Lifestyle"])


# -----------------------------
# UI Helpers
# -----------------------------
def display_recommendation_mode(data):
    st.subheader(data["title"])
    st.write(data["summary"])

    st.markdown("### Ranked recommendations")

    for idx, item in enumerate(data["items"], start=1):
        with st.container(border=True):
            col1, col2, col3 = st.columns([2.2, 1, 1])

            with col1:
                st.markdown(f"### {idx}. {item['name']}")
                st.write(f"**Why people like it:** {item['why']}")
                st.write(f"**Best for:** {item['best_for']}")
                st.write(f"**Watch out:** {item['watch_out']}")

            with col2:
                st.metric("Confidence", f"{item['score']}/100")

            with col3:
                st.metric("Sentiment", item["sentiment"])

            st.markdown("**Comment pattern**")
            st.write(item["comment_pattern"])

            st.markdown("**Representative comments**")
            for quote in item["quotes"]:
                st.info(quote)


def display_insight_mode(query, category, result):
    positive, neutral, negative = result["sentiment"]

    st.subheader(f"Insight report: {query}")
    st.caption(f"Smart category detected: {category}")

    st.markdown("### Quick summary")
    st.write(result["summary"])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Positive", f"{positive}%")
    col2.metric("Neutral", f"{neutral}%")
    col3.metric("Negative", f"{negative}%")
    col4.metric("Confidence", f"{result['confidence']}/100")

    st.progress(positive / 100)

    st.markdown("### Comment Confidence Analysis")
    st.write(result["confidence_reason"])

    left, right = st.columns(2)

    with left:
        st.markdown("### What people like")
        for item in result["likes"]:
            st.write(f"✅ {item}")

    with right:
        st.markdown("### Common complaints")
        for item in result["complaints"]:
            st.write(f"⚠️ {item}")

    st.markdown("### Key comment themes")
    theme_cols = st.columns(len(result["themes"]))
    for i, theme in enumerate(result["themes"]):
        theme_cols[i].button(theme, disabled=True)

    st.markdown("### Decision signal")
    st.success(result["decision_signal"])

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### Risk signals")
        for risk in result["risk_signals"]:
            st.write(f"🚩 {risk}")

    with col_b:
        st.markdown("### Actionable recommendations")
        for rec in result["recommendations"]:
            st.write(f"💡 {rec}")

    st.markdown("### Representative comments")
    for quote in result["quotes"]:
        st.info(quote)

    st.markdown("### Best-fit audience")
    st.success(result["persona"])


# -----------------------------
# Main App
# -----------------------------
st.title("🔍 CommentLens")
st.caption("Turn social comments into decision-ready consumer insights.")

st.markdown(
    """
    CommentLens helps users understand what people really say about any topic.  
    It supports two MVP modes:

    **Recommendation Mode** — for queries like “Chicago coffee shops” or “杭州餐厅,” returning specific ranked recommendations.  
    **Insight Mode** — for products, brands, schools, travel topics, and lifestyle searches, returning sentiment, risks, themes, representative comments, and confidence analysis.
    """
)

st.divider()

st.markdown("### Try a search")

suggestions = [
    "芝加哥咖啡馆",
    "杭州咖啡馆",
    "Lululemon leggings",
    "敏感肌面霜",
    "MBA申请"
]

if "query" not in st.session_state:
    st.session_state["query"] = ""

cols = st.columns(len(suggestions))
for i, suggestion in enumerate(suggestions):
    if cols[i].button(suggestion):
        st.session_state["query"] = suggestion

query = st.text_input(
    "Search any topic",
    value=st.session_state["query"],
    placeholder="e.g., 芝加哥咖啡馆, 杭州餐厅, Aritzia, MBA申请, 敏感肌面霜..."
)

analyze = st.button("Analyze comments", type="primary")

if analyze:
    if not query.strip():
        st.warning("Please enter a topic first.")
    else:
        st.divider()

        recommendation_data = get_recommendations(query)

        if recommendation_data:
            st.caption(f"Detected mode: {recommendation_data['mode']}")
            display_recommendation_mode(recommendation_data)

        else:
            category = classify_query(query)
            result = generate_insights(query, category)
            st.caption("Detected mode: Insight Mode")
            display_insight_mode(query, category, result)

        st.divider()
        st.markdown("### MVP note")
        st.write(
            "This demo currently uses a rule-based smart query router and curated mock comment patterns to simulate the product experience without paid APIs. "
            "In the next version, this layer can be replaced by a live LLM/search API and real social-comment data."
        )

else:
    st.info("Enter a topic or click a trending search to start.")        "Travel": {
            "sentiment": (72, 18, 10),
            "likes": [
                "Scenic spots and photo-friendly locations are frequently praised.",
                "Users mention strong food, cafe, and short-trip potential.",
                "Many comments frame it as a good weekend or holiday destination."
            ],
            "complaints": [
                "Crowds during holidays are the most common complaint.",
                "Transportation and itinerary planning can be tiring.",
                "Some popular spots are described as over-commercialized."
            ],
            "quotes": [
                f"“{query} is beautiful, but I would avoid peak season.”",
                f"“The hidden local spots are more interesting than the famous ones.”",
                f"“Great for photos, but planning ahead really matters.”"
            ],
            "persona": "Best for weekend travelers, couples, foodies, and photo lovers."
        },
        "Beauty": {
            "sentiment": (64, 22, 14),
            "likes": [
                "Texture, packaging, and ease of daily use are frequently mentioned.",
                "Users value visible but gradual improvement.",
                "Repeat purchase intention appears when price is reasonable."
            ],
            "complaints": [
                "Effectiveness varies by skin type.",
                "Price sensitivity is high.",
                "Some users say the product requires consistent use to see results."
            ],
            "quotes": [
                f"“{query} feels nice, but it is not a miracle product.”",
                f"“I would repurchase if there is a discount.”",
                f"“It worked for me, but skin type really matters.”"
            ],
            "persona": "Best for skincare beginners, sensitive-skin users, and value-conscious buyers."
        },
        "Food": {
            "sentiment": (69, 20, 11),
            "likes": [
                "Taste, atmosphere, and social-sharing value are frequently praised.",
                "Users often recommend it for friend gatherings.",
                "Visual presentation and store vibe drive strong interest."
            ],
            "complaints": [
                "Long waiting time is a recurring issue.",
                "Some users question value for money.",
                "Experience may vary by location or time of visit."
            ],
            "quotes": [
                f"“{query} is worth trying, but go early to avoid the line.”",
                f"“The vibe is great for photos.”",
                f"“Taste is good, but the price is slightly high.”"
            ],
            "persona": "Best for foodies, friend gatherings, and social media users."
        },
        "Fashion": {
            "sentiment": (67, 21, 12),
            "likes": [
                "Design, fit, and daily wearability are frequently mentioned.",
                "Brand image creates strong purchase interest.",
                "Users like items that are easy to style."
            ],
            "complaints": [
                "Sizing can be inconsistent.",
                "Price is a major concern.",
                "Some users question durability or cost-performance."
            ],
            "quotes": [
                f"“{query} looks good, but size selection matters.”",
                f"“I like the style, but I waited for a sale.”",
                f"“Very wearable for daily outfits.”"
            ],
            "persona": "Best for young professionals, lifestyle shoppers, and trend followers."
        },
        "Education": {
            "sentiment": (61, 27, 12),
            "likes": [
                "Users care most about outcomes, career value, and peer experience.",
                "Practical application advice receives strong engagement.",
                "First-hand experience is considered more trustworthy than generic guides."
            ],
            "complaints": [
                "Cost and uncertainty are major concerns.",
                "The application process feels stressful.",
                "Information quality varies significantly across posts."
            ],
            "quotes": [
                f"“{query} is valuable, but you need to be clear about your goal.”",
                f"“The most useful posts are from people who actually went through it.”",
                f"“Cost is the biggest thing to consider.”"
            ],
            "persona": "Best for applicants, career switchers, and international students."
        },
        "Tech": {
            "sentiment": (66, 24, 10),
            "likes": [
                "Users are curious about productivity gains and practical use cases.",
                "Early adopters share detailed workflows.",
                "Clear tutorials and examples increase trust."
            ],
            "complaints": [
                "Some users are confused about setup.",
                "Trust and accuracy concerns remain.",
                "Users want more examples before paying."
            ],
            "quotes": [
                f"“{query} is useful once you know the right workflow.”",
                f"“The idea is cool, but onboarding could be better.”",
                f"“I want more examples before paying for it.”"
            ],
            "persona": "Best for students, creators, productivity users, and early adopters."
        },
        "Lifestyle": {
            "sentiment": (58, 29, 13),
            "likes": [
                "Users show broad curiosity and emotional engagement.",
                "Many posts focus on personal experience and decision-making.",
                "The topic is useful for discovering trends and consumer pain points."
            ],
            "complaints": [
                "Comments are scattered and subjective.",
                "General searches need stronger filtering.",
                "Users often disagree depending on personal preference."
            ],
            "quotes": [
                f"“{query} has mixed reviews, so I checked multiple posts.”",
                f"“The comments are more useful than the post itself.”",
                f"“It depends a lot on personal preference.”"
            ],
            "persona": "Best for trend explorers, casual researchers, and consumer insight users."
        }


    return templates.get(category, templates["Lifestyle"])


# -----------------------------
# UI
# -----------------------------
st.title("🔍 CommentLens")
st.caption("Turn social comments into consumer insights — fast, structured, and searchable.")

st.markdown(
    """
    CommentLens helps users understand what people really say about any topic by summarizing 
    social-style comments into sentiment, likes, complaints, representative quotes, and best-fit audiences.
    """
)

st.divider()

st.markdown("### Try a trending search")

suggestions = [
    "杭州三日游",
    "Lululemon leggings",
    "芝加哥咖啡馆",
    "敏感肌面霜",
    "MBA申请"
]

cols = st.columns(len(suggestions))

if "query" not in st.session_state:
    st.session_state["query"] = ""

for i, suggestion in enumerate(suggestions):
    if cols[i].button(suggestion):
        st.session_state["query"] = suggestion

query = st.text_input(
    "Search any topic",
    value=st.session_state["query"],
    placeholder="e.g., 杭州, Aritzia, Chicago brunch, MBA application..."
)

analyze = st.button("Analyze comments", type="primary")

if analyze:
    if not query.strip():
        st.warning("Please enter a topic first.")
    else:
        category = classify_query(query)
        result = generate_insights(query, category)

        positive, neutral, negative = result["sentiment"]

        st.divider()

        st.subheader(f"Analysis for: {query}")
        st.caption(f"Smart category detected: {category}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Positive", f"{positive}%")
        col2.metric("Neutral", f"{neutral}%")
        col3.metric("Negative", f"{negative}%")

        st.progress(positive / 100)

        left, right = st.columns(2)

        with left:
            st.markdown("### ✅ What people like")
            for item in result["likes"]:
                st.write(f"- {item}")

        with right:
            st.markdown("### ⚠️ Common complaints")
            for item in result["complaints"]:
                st.write(f"- {item}")

        st.markdown("### 💬 Representative comments")
        for quote in result["quotes"]:
            st.info(quote)

        st.markdown("### 🎯 Best-fit audience")
        st.success(result["persona"])

        st.markdown("### Product note")
        st.write(
            "This MVP uses a rule-based smart query router to simulate open-ended topic understanding. "
            "In the next version, this layer can be replaced by an LLM API for real-time semantic analysis."
        )

else:
    st.info("Enter a topic or click a trending search to start.")
