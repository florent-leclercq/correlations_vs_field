# correlations_vs_field #

[![arXiv](https://img.shields.io/badge/astro--ph.CO-arxiv%3A2103.xxxxx-B31B1B.svg?style=flat)](https://arxiv.org/abs/2103.xxxxx)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/florent-leclercq/correlations_vs_field/blob/main/LICENSE)
[![Website florent-leclercq.eu](https://img.shields.io/website-up-down-green-red/http/florent-leclercq.eu.svg)](http://florent-leclercq.eu/)

Correlation functions versus field-level inference in cosmology: example with log-normal fields

## Documentation ##

This is a companion repository to Leclercq & Heavens 2021, *On the accuracy and precision of correlation functions and field-level inference in cosmology*, <a href="http://arxiv.org/pdf/2103.xxxxx" class="document" target="blank">arXiv:2103.xxxxx</a>.

The code contains a python library for log-normal fields, [libLN.py](libLN.py) and two example configuration files: [config_10.py](config_10.py) (alpha=1.0) and [config_02.py](config_02.py) (alpha=0.2). The main part of the code is split into several Jupyter notebooks:
* [Inference_Summaries.ipynb](Inference_Summaries.ipynb): likelihood-based analysis of the two-point correlation functions (section 3 in Leclercq & Heavens 2021)
* [Inference_SBI.ipynb](Inference_SBI.ipynb): simulation-based inference using the two-point correlation functions (section 4 in Leclercq & Heavens 2021)
* Inference_DA_*.ipynb: field-level inference with data assimilation (section 5 in Leclercq & Heavens 2021)
* [Plots.ipynb](Plots.ipynb): code to produce the plots of the paper, and some more

The raw data (pools of simulations for simulation-based inference and Markov Chains for data assimilation) are not stored in this repository due to their large size. They are available upon reasonable request to the corresponding author.

In addition to usual python packages such as numpy, scipy, matplotlib, pickle, code has the following dependencies:
* [pydelfi](https://github.com/justinalsing/pydelfi) and [ELFI](https://github.com/elfi-dev/elfi) for simulation-based inference ([Inference_SBI.ipynb](Inference_SBI.ipynb))
* [pymc3](https://docs.pymc.io) for data assimilation (Inference_DA_*.ipynb)

## Contributors ##

* Florent Leclercq, florent.leclercq@polytechnique.org
* Alan Heavens

## Reference ##


To acknowledge the use of this software, please cite the paper <a href="http://arxiv.org/pdf/2103.xxxxx" class="document" target="blank">Leclercq & Heavens (2021)</a>: 

*On the accuracy and precision of correlation functions and field-level inference in cosmology*<br/>
F. Leclercq, A. Heavens<br/>
<a href="http://arxiv.org/abs/2103.xxxxx" target="blank">arXiv:2103.xxxxx</a> [<a href="http://arxiv.org/abs/2103.xxxxx" target="blank">astro-ph.CO</a>] [<a href="https://ui.adsabs.harvard.edu/?#abs/xxxxxxx" target="blank">ADS</a>] [<a href="http://arxiv.org/pdf/2103.xxxxx" class="document" target="blank">pdf</a>]

    @ARTICLE{correlations_vs_field,
        author = {{Leclercq}, Florent and {Heavens}, Alan},
        title = "{On the accuracy and precision of correlation functions and field-level inference in cosmology}",
        eprint = {2103.xxxxx},
        }



## License ##

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. By downloading and using pySELFI, you agree to the [LICENSE](LICENSE), distributed with the source code in a text file of the same name.
