## Sub-SA: Strengthen In-context Learning via Submodular Selective Annotation

Published ECAI 2024 : https://arxiv.org/abs/2407.05693


In-context learning (ICL) leverages in-context examples
as prompts for the predictions of Large Language Models (LLMs).
These prompts play a crucial role in achieving strong performance.
However, the selection of suitable prompts from a large pool of labeled
examples often entails significant annotation costs. To address this
challenge, we propose Sub-SA (Submodular Selective Annotation), a
submodule-based selective annotation method. The aim of Sub-SA is
to reduce annotation costs while improving the quality of in-context
examples and minimizing the time consumption of the selection process. In Sub-SA, we design a submodular function that facilitates
effective subset selection for annotation and demonstrates the characteristics of monotonically and submodularity from the theoretical perspective. Specifically, we propose RPR (Reward and Penalty
Regularization) to better balance the diversity and representativeness
of the unlabeled dataset attributed to a reward term and a penalty
term, respectively. Consequently, the selection for annotations can
be effectively addressed with a simple yet effective greedy search
algorithm based on the submodular function. Finally, we apply the
similarity prompt retrieval to get the examples for ICL. Compared
to existing selective annotation approaches, Sub-SA offers two main
advantages. (1.) Sub-SA operates in an end-to-end, unsupervised
manner, and significantly reduces the time consumption of the selection process (from hours-level to millisecond-level). (2.) Sub-SA
enables a better balance between data diversity and representativeness
and obtains state-of-the-art performance. Meanwhile, the theoretical support guarantees their reliability and scalability in practical
scenarios. Extensive experiments conducted on diverse models and
datasets demonstrate the superiority of Sub-SA over previous methods, achieving millisecond(ms)-level time selection and remarkable
performance gains. The efficiency and effectiveness of Sub-SA make
it highly suitable for real-world ICL scenarios.

![pipeline](img/pipeline.png)


![subsa](img/subsa.png)



Run Code:

	```
        python main.py  \
        --model_cache_dir models \
        --data_cache_dir datasets \
        --task_name rte \
        --selective_annotation_method diversity \
        --prompt_retrieval_method similar \
        --annotation_size 18 \
        --cuda_id 0 \
        --model_name EleutherAI/gpt-j-6B \
        --seed 1  \
	```

Cite: 

    '''@article{qian2024sub,
  title={Sub-SA: Strengthen In-context Learning via Submodular Selective Annotation},
  author={Qian, Jian and Sun, Miao and Zhou, Sifan and Zhao, Ziyu and Hun, Ruizhi and Chiang, Patrick},
  journal={arXiv preprint arXiv:2407.05693},
  year={2024}
}'''
