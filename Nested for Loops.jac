walker init{
     treatment = file.load_json("data.json");
        your_treatment = "";
        treatments = "";
        lists_treatment = treatment[0]['Treatment'];
        e = 0;
        v = 0;
        
       
       for i in treatment{
            e = e;
            lists_treatment = treatment[e]['Treatment']; 

            for i in lists_treatment{
                v = v;
                treatments += lists_treatment[v]["Treatment"];
                v += 1;
        }
            your_treatment += treatment[e]["Disease/Illness"] + treatments;
            e += 1;
            v = 0;
       }
        report{"Treatment for your Illness": your_treatment};
}