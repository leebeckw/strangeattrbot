# strangeattrbot

little [twitter bot](https://twitter.com/strangeattrbot) sporadically posting strange attractors

method from [Sprott (1993)](https://sprott.physics.wisc.edu/pubs/PAPER203.HTM)

a few code snippets from [here](https://github.com/icecolbeveridge/strangeAttractors)

### more details

this code iteratively generates points using the follow quadratic equations:

x<sub>n+1</sub> = a<sub>1</sub> + a<sub>2</sub>x<sub>n</sub> + a<sub>3</sub>x<sub>n</sub><sup>2</sup> + a<sub>4</sub>x<sub>n</sub>y<sub>n</sub> + a<sub>5</sub>y<sub>n</sub> + a<sub>6</sub>y<sub>n</sub><sup>2</sup>

y<sub>n+1</sub> = a<sub>7</sub> + a<sub>8</sub>y<sub>n</sub> + a<sub>9</sub>y<sub>n</sub><sup>2</sup> + a<sub>10</sub>y<sub>n</sub>x<sub>n</sub> + a<sub>11</sub>x<sub>n</sub> + a<sub>12</sub>x<sub>n</sub><sup>2</sup>

the initial point is (0.05, 0.05) and the equations are each run 100,000 times to generate 100,000 points which are then plotted

the coefficients (a<sub>1</sub>...a<sub>12</sub>) are randomly chosen; their values are in the range [-1.2, 1.2], rounded to one decimal place

each value is assigned a letter A->Y; for example -1.2 = A; -1.1 = B ... 1.1 = X; 1.2 = Y

thus, each image's associated 12-letter string can be translated into the  coefficients for the equations

the majority of coefficients are likely to produce uninteresting behavior (converging to a fixed point or points diverging to infinity)

so, if you came up with a certain 12-letter word or combination of words, it is likely that it would not demonstrate chaotic behavior

in order to identify the coefficients for which these equations produce a complicated, yet bounded set of points, we can calculate the Lyapunov exponent, which can be thought of as "the rate at which information about the initial condition is lost, or equivalently, the rate at which the accuracy of a prediction declines as one projects farther into the future" (Sprott 1993)

only those coefficient sets for which the Lyapunov exponent is above 0.001 are considered "chaotic" for these purposes

it is estimated that around 1.6% of the possible coefficient sets are chaotic, or approximately 10<sup>15</sup> cases. as Sprott writes, "viewing them all at a rate of one per second would require over 30 million years!" it is highly likely that all of the images posted by this bot are unique.

### sample images

AGVTEVQRUITD
![AGVTEVQRUITD](https://github.com/leebeckw/strangeattrbot/blob/main/sample_imgs/swallow.png?raw=true)

VKKUKGGBOLLN
![VKKUKGGBOLLN](https://github.com/leebeckw/strangeattrbot/blob/main/sample_imgs/tri.png?raw=true)

#### citations

Sprott, J. C. (1993). Automatic generation of strange attractors. Computers & Graphics, 17(3), 325-332.