walker init{
    answers = file.load_json("Agencies.json");
    e = 0;
    name = [""];
    names = "";
    namess = {};
    for i in answers{
        e = e;
        name.list::append(answers[e]["Medical_Agency"]);
        names += answers[e]["Medical_Agency"] +",  ";
        namess[answers[e]["Medical_Agency"]] = answers[e]["Email_or_website"];
        e += 1; 
    }
    report{"Future Prompt Method": name};
    report{"Future Prompt Method": names};
    report{"Future Prompt Method": namess};
}