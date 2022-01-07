# strangeattrbot

little [twitter bot](https://twitter.com/strangeattrbot) sporadically posting strange attractors

method from [Sprott (1993)](https://sprott.physics.wisc.edu/pubs/PAPER203.HTM)

requirements at [strangeattrbot-reqs.yml](/strangeattrbot-reqs.yml)

a few code snippets from [here](https://github.com/icecolbeveridge/strangeAttractors)

### more details

this code iteratively generates points using the follow quadratic equations:
x<sub>n+1</sub> = a<sub>1</sub> + a<sub>2</sub>x<sub>n</sub> + a<sub>3</sub>x<sub>n</sub><sup>2</sup> + a<sub>4</sub>x<sub>n</sub>y<sub>n</sub> + a<sub>5</sub>y<sub>n</sub> + a<sub>6</sub>y<sub>n</sub><sup>2</sup>
y<sub>n+1</sub> = a<sub>7</sub> + a<sub>8</sub>y<sub>n</sub> + a<sub>9</sub>y<sub>n</sub><sup>2</sup> + a<sub>10</sub>y<sub>n</sub>x<sub>n</sub> + a<sub>11</sub>x<sub>n</sub> + a<sub>12</sub>x<sub>n</sub><sup>2</sup>

the initial point is (0.05, 0.05)

the coefficients are randomly chosen in increments of 0.1 in the range [-1.2, 1.2]

each value is assigned a letter A->Y; for example -1.2 = A; -1.1 = B ... 1.1 = X; 1.2 = Y

thus, each image's associated 12-letter string can be translated into its associated coefficients

### sample images

[](/swallow.png)
AGVTEVQRUITD

[](/tri.png)
VKKUKGGBOLLN