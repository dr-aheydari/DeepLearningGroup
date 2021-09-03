# UCM Applied Math Deep Learning Group (DLG)
This repo hosts the material and references covered in the DLG learning group in Fall 2021. This `README` will be updated regularly before each meeting, so please check back for more information and resources. Contributions to this repo will also be greatly appreciated, so please feel free to fork and pull request with any updates you find necessary. ***Please star ⭐️ the repository for staying tuned with the updates***

### [Click here](https://github.com/dr-aheydari/DeepLearningGroup#learning-resources) for jumping to the reading list

## General Information
The main objective of the learning group is to dive deeper into fundamentals of Machine Learning (Deep Learning in particular) through a mathematical lens. This group will provide a forum for graduate students, postdocs and faculty interested in Deep Learning to learn about the fundamentals and advances in the field while fostering broader discussions and collaborations. This group is organized by [Ali Heydari](https://www.ali-heydari.com/about). 
 
##### Meeting times:
 
The group will meet Fridays from 11:00am-12:30pm in ACS 362B, beginning September 3rd. 
 
##### Meeting format:
 
The first half hour of the sessions will be dedicated to reading, followed by discussions of the topics. This format is intended to provide a dedicated time for participants to read about the specific topics during each session, so that all can engage in fruitful discussions and contribute to the group’s collective learning. Given the time constraints however, *participants are expected to have a working knowledge of machine learning and other relevant prerequisites*. 
 
#### Meeting Meta Topics:
 
Given the broad range of topics and the short amount of time, we would like to tailor each session to address the interest of the audience in the following meta topics: 
 
1. Universal Approximation Theorem
1. Evaluation of ML/DL Models
1. Optimization in Deep Learning
1. Deep Learning in Computer Vision
1. Deep Learning in Natural Language Processing

## Learning Resources 
Here we provide a list of hand-picked resources for each of the meeting sessions, in addition to references for pre-requisites needed before attending the sessions. Per UC Merced's policy, the links will expire in 90 days. However, we have included the citations to each paper in the Acknowledgment section. 

| Meeting Date    | Meeting Topic                            | Reading Resources                                                                                                                                                                                                                                                            | Pre-Requisites                                                                                                        |  Additional Notes  |
|-----------------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---|
| Sep. 3rd, 2021  | Universal Approximation Theorem          | [Ref 1](https://merced-my.sharepoint.com/:b:/g/personal/aheydari_ucmerced_edu/EUe04trpsRlHqx7lnTxiikEBwo3s2Ws-MFFtoRRFIvl2uw?e=uUyQgY), [Ref 2](https://merced-my.sharepoint.com/:b:/g/personal/aheydari_ucmerced_edu/EbnJZcdaHDJHqxE0XEZQf_oB0EmMYFc_PmL36qERWDc1ZA?e=lhz8iE)  | [Ref i](https://www.deeplearningbook.org/contents/ml.html), [Ref ii](https://www.deeplearningbook.org/contents/mlp.html), [Ref iv](https://merced-my.sharepoint.com/:b:/g/personal/aheydari_ucmerced_edu/EX7ifasirRpMleiwtHQnRFMBmuwMpsFsyLJdY9D4gyzWMw?e=ZXILha)|   |
| Sep. 10th, 2021 | Universal Approximation Theorem (Continuation of last week) | [Ref iii (main)](https://merced-my.sharepoint.com/:b:/g/personal/aheydari_ucmerced_edu/EUoLVWEJ7gtFspFOS7ovosABbdkFBxdx3S3eh45XwBUQ5g?e=xFKy3b) [Ref 3](https://merced-my.sharepoint.com/:b:/g/personal/aheydari_ucmerced_edu/ETtZ9P-0AI1Fu5uSvU5OAbABlAJ1gad5lpcyBhuGhlLNFg?e=ewgL8K), [Ref 4](https://merced-my.sharepoint.com/:b:/g/personal/aheydari_ucmerced_edu/Ea8_iJPFK8JEmiddCPFnk0MB9q9mS-uC66mDIkrtnOQN5g?e=UdtTeB) | [Ref i](https://www.deeplearningbook.org/contents/ml.html), [Ref ii](https://www.deeplearningbook.org/contents/mlp.html), [Ref iv](https://merced-my.sharepoint.com/:b:/g/personal/aheydari_ucmerced_edu/EX7ifasirRpMleiwtHQnRFMBmuwMpsFsyLJdY9D4gyzWMw?e=ZXILha) |   |
| Sep. 17th, 2021 | Appropriate Metrics and Model Evaluation | Coming soon                                                                                                                                                                                                                                                                  | [ref1](https://www.deeplearningbook.org/contents/ml.html), [ref2](https://www.deeplearningbook.org/contents/mlp.html) |   |
|   Sep. 24th, 2021             |     Appropriate Metrics and Model Evaluation | Coming soon                                                                                                                                                                                                                                                                          |                                                                                                                       |   |



## Acknowledgements and References

### Universal Approximation Theory

````
@article{Ref 1,
	abstract = {This paper deals with the approximation behaviour of soft computing techniques. First, we give a survey of the results of universal approximation theorems achieved so far in various soft computing areas, mainly in fuzzy control and neural networks. We point out that these techniques have common approximation behaviour in the sense that an arbitrary function of a certain set of functions (usually the set of continuous function, C) can be approximated with arbitrary accuracy ε on a compact domain. The drawback of these results is that one needs unbounded numbers of ``building blocks'' (i.e. fuzzy sets or hidden neurons) to achieve the prescribed ε accuracy. If the number of building blocks is restricted, it is proved for some fuzzy systems that the universal approximation property is lost, moreover, the set of controllers with bounded number of rules is nowhere dense in the set of continuous functions. Therefore it is reasonable to make a trade-off between accuracy and the number of the building blocks, by determining the functional relationship between them. We survey this topic by showing the results achieved so far, and its inherent limitations. We point out that approximation rates, or constructive proofs can only be given if some characteristic of smoothness is known about the approximated function.},
	author = {Domonkos Tikk and L{\'a}szl{\'o} T. K{\'o}czy and Tam{\'a}s D. Gedeon},
	doi = {https://doi.org/10.1016/S0888-613X(03)00021-5},
	issn = {0888-613X},
	journal = {International Journal of Approximate Reasoning},
	keywords = {Universal approximation performed by fuzzy systems and neural networks, Kolmogorov's theorem, Approximation behaviour of soft computing techniques, Course of dimensionality, Nowhere denseness, Approximation rates, Constructive proofs},
	number = {2},
	pages = {185-202},
	title = {A survey on universal approximation and its limits in soft computing techniques},
	url = {https://www.sciencedirect.com/science/article/pii/S0888613X03000215},
	volume = {33},
	year = {2003},
	Bdsk-Url-1 = {https://www.sciencedirect.com/science/article/pii/S0888613X03000215},
	Bdsk-Url-2 = {https://doi.org/10.1016/S0888-613X(03)00021-5}}

````

````
@article{Ref 2,
	abstract = {In this paper, we present a review of some recent works on approximation by feedforward neural networks. A particular emphasis is placed on the computational aspects of the problem, i.e. we discuss the possibility of realizing a feedforward neural network which achieves a prescribed degree of accuracy of approximation, and the determination of the number of hidden layer neurons required to achieve this accuracy. Furthermore, a unifying framework is introduced to understand existing approaches to investigate the universal approximation problem using feedforward neural networks. Some new results are also presented. Finally, two training algorithms are introduced which can determine the weights of feedforward neural networks, with sigmoidal activation neurons, to any degree of prescribed accuracy. These training algorithms are designed so that they do not suffer from the problems of local minima which commonly affect neural network learning algorithms.},
	author = {Franco Scarselli and Ah {Chung Tsoi}},
	doi = {https://doi.org/10.1016/S0893-6080(97)00097-X},
	issn = {0893-6080},
	journal = {Neural Networks},
	keywords = {Approximation by neural networks, Approximation of polynomials, Constructive approximation, Feedforward neural networks, Multilayer neural networks, Radial basis functions, Universal approximation},
	number = {1},
	pages = {15-37},
	title = {Universal Approximation Using Feedforward Neural Networks: A Survey of Some Existing Methods, and Some New Results},
	url = {https://www.sciencedirect.com/science/article/pii/S089360809700097X},
	volume = {11},
	year = {1998},
	Bdsk-Url-1 = {https://www.sciencedirect.com/science/article/pii/S089360809700097X},
	Bdsk-Url-2 = {https://doi.org/10.1016/S0893-6080(97)00097-X}}
````

````
@book{Ref i-Ref ii,
        title={Deep Learning},
        author={Ian Goodfellow and Yoshua Bengio and Aaron Courville},
        publisher={MIT Press},
        note={\url{http://www.deeplearningbook.org}},
        year={2016}
 }

````

````
@article{Ref iii,
	abstract = {In this paper we demonstrate that finite linear combinations of compositions of a fixed, univariate function and a set of affine functionals can uniformly approximate any continuous function ofn real variables with support in the unit hypercube; only mild conditions are imposed on the univariate function. Our results settle an open question about representability in the class of single hidden layer neural networks. In particular, we show that arbitrary decision regions can be arbitrarily well approximated by continuous feedforward neural networks with only a single internal, hidden layer and any continuous sigmoidal nonlinearity. The paper discusses approximation properties of other possible types of nonlinearities that might be implemented by artificial neural networks.},
	author = {Cybenko, G. },
	da = {1989/12/01},
	date-added = {2021-09-02 13:04:35 -0700},
	date-modified = {2021-09-02 13:04:35 -0700},
	doi = {10.1007/BF02551274},
	id = {Cybenko1989},
	isbn = {1435-568X},
	journal = {Mathematics of Control, Signals and Systems},
	number = {4},
	pages = {303--314},
	title = {Approximation by superpositions of a sigmoidal function},
	ty = {JOUR},
	url = {https://doi.org/10.1007/BF02551274},
	volume = {2},
	year = {1989},
	Bdsk-Url-1 = {https://doi.org/10.1007/BF02551274}}
````

````
@book{Ref iv,
        title={Infinite Dimensional Analysis: A Hitchhiker’s Guide},
        author={Charalambos D. AliprantisKim C. Border},
        publisher={Springer},
        note={\url{https://link.springer.com/book/10.1007%2F3-540-29587-9}},
        year={2006}
 }
````
