walker init{
    can t5_sum.classify_text;
    has text;
    has min_length = 30;
    has max_length = 1000;
    
    answers = file.load_json("data.json");
    e = 0;
    symptoms = [""];
    for i in answers{
        e = e;
        text = answers[e]["Symptoms"][0];
        summarized_text = t5_sum.classify_text(text=text, min_length=min_length, max_length=max_length);
        symptoms.list::append(summarized_text);
        e += 1;
    }
    

    report {"Your Symptoms": symptoms};
}