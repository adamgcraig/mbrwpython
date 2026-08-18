A Memory-Biased Random Walk (MBRW) is an alternative to a simple random walk on an unweighted network.
In MBRW, the walk agent is more likely by a factor of alpha to take a path that it has encountered within the past S steps.
Random walks have a variety of uses in network analysis.
The prior works below have shown that MBRW is more sensitive to network community structure than is a simple random walk, because memory amplifies the ability of communities to trap the walk agent.
The original implementations of MBRW community detection were in MATLAB.
Yucel, M., & Hershberg, U. (2014). Memory as an organizer of dynamic modules in a network of potential interactions. SCW at AAMAS.
Yucel, M., Muchnik, L., & Hershberg, U. (2017). Detection of network communities with memory-biased random walk algorithms. Journal of Complex Networks, 5(1), 48-69.
The original implementation of MBRW multispectral analysis used C++ for the MBRW agent simulation itself and any other computationally intensive steps and MATLAB for data preprocessing and the final, simple steps of the calculations.
Craig, A., Yücel, M., Muchnik, L., & Hershberg, U. (2022). Impact of finite size effect on applicability of generalized fractal and spectral dimensions to biological networks. Chaos, Solitons & Fractals, 164, 112707.
This Python library provides both community detection and spectral dimension calculation in one easy-to-use Python package.
