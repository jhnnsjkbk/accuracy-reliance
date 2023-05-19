# Official implementation for the paper "On the Interdependence of Reliance Behavior and Accuracy in AI-Assisted Decision-Making"

### Abstract
In AI-assisted decision-making, a central promise of putting a human in the loop is that they should be able to complement the AI system by adhering to its correct and overriding its mistaken recommendations. In practice, however, we often see that humans tend to over- or under-rely on AI recommendations, meaning that they either adhere to wrong or override correct recommendations. Such reliance behavior is detrimental to decision-making accuracy. In this work, we articulate and analyze the interdependence between reliance behavior and accuracy in AI-assisted decision- making, which has been largely neglected in prior work. We also propose a visual framework to make this interdependence more tangible. We apply the framework to interpret and deepen the understanding of existing empirical findings, as well as obtain a nuanced understanding of the effects of interventions (e.g., explanations) in AI-assisted decision-making. Finally, we infer several interesting properties from the framework: (i) when humans under-rely on AI recommendations, there may be no possibility for them to complement the AI in terms of decision-making accuracy; (ii) when humans cannot discern correct and wrong AI recommendations, no such improvement can be expected either; (iii) interventions may lead to an increase in decision-making accuracy that is solely driven by an increase in humans’ adherence to AI recommendations, without any ability to discern correct and wrong. Our work emphasizes the importance of measuring and reporting both effects on accuracy and reliance behavior when empirically assessing interventions.

### Implementation of the framework

We make use of standard packages and provide a simple user interfact to define values passed to our framework. The framework will be visualized according to the values specified by the user. In addition, the implementation allows to calculate characterstics of the reliance behavior (like the proportion of wrong overrides) and the quality of reliance specifiying the ability to discern correct from wrong AI recommendations. 

### Required packages
- numpy
- matplotlib
- tkinter
- math

### Please cite as 
Schoeffer, J., Jakubik, J., Voessing, M., Kuehl, N., & Satzger, G. (2023). On the Interdependence of Reliance Behavior and Accuracy in AI-Assisted Decision-Making. Hybrid Human Artificial Intelligence (HHAI) 2023.
