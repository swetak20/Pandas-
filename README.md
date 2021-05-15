# Pandas-
Using pandas to predict the winner of Galaxy.


## Problem Statement:

So Galaxy is around the corner and the campus junta is enthusiastic about the same, different HECs of halls are doing their best to win the GC, now, in the middle of the galactic chaos, ACA announces the semester long projects and some hall loving people pledge to contribute for the very cause of the welfare of the Hall (_"Hall hamari maata hai!"_).

With this, strategic thinkers want to know the chances of the winning by conducting various surveys in their respective halls, you are given the `galaxy_data.csv` file containing the dataset of the surveys of different halls. You are the god of designing utilities for the different HECs and your job is to predict the winner of the event _(you'll be given kathi rolls for the same)_. Following are the key features about the data (to protect the privacy, survey people hid the names of the people surveyed):

1. ***The dataset has columns as***: 

***Hall Practice_hours,  Posts_shared,  Bulla_hours, Classes_missed,  Relationship_status, Enthu***

  - **Hall:** This is the hall of the student surveyed.
  - **Practice_hours (out of max 20):** Since practice hours (dance, singing, debating) are important, the weight of this factor will be **0.4**.
  - **Posts_shared (out of max 10):** Your responsibility towards your hall is evident from the social advertising factor, the most posts you  share, the better asset you are for your Hall, this factor has a weight of **0.2**.
  - **Bulla_hours (out of max 10):** Bonding with the hall environment requires a certain amount of bulla and evilish hall bitching, HEC wants people to develop jihaad among them, this factor incorporates **0.2** weight for the enthu factor.
  - **Classes_missed (out of max 8):** HEC takes care of academics as well, it is assumed that students who miss a hell lot of classes might end up in depression and run away from galaxy, thus, this factor contributes **-0.2** weight towards the enthu factor.
  - **Relationship_status:** HEC knows that February is coming, and so is the valentine's week, they know that committed people will ditch the Hall for their _special one_ (or for _"meri wali alag hai"_), thus, they keep record about the relationship status of the students, there are 3 categories of people with 3 different weights for the enthu contribution:
    - _Single and stud:_ These are the prime asset for the hall, they will contribute **0.2** weight towards the enthu factor.
    - _Committed inside campus:_ These are the snake people, and HEC knows they can leak the information and can be the cause for the Hall losing, their toxicity will contribute **-0.2** towards the enthu factor.
    - _Long distance ones:_ These are the people who are neither toxic, nor useful, they will contibute **ZERO** weight in the enthu factor.
2. ***What is the enthu factor?***

This will be the weighted mean of all the factors mentioned above. For eg. a person with the following stats:

```
Hall: 12
Practice_hours (ph): 11
Posts_shared (ps): 4
Bulla_hours (bh): 4
Classes_missed (cm): 2
Relationship_status (rs): SINGLE_AND_STUD
```

will have the enthu of that person as **enthu = (11/20)x(0.4) + (4/10)x(0.2) + (4/10)x(0.2) + (2/8)x(-0.2) + (0.2)**

_enthu = 0.4100 

***Note that relationship status will contribute directy, i.e. 0.2, -0.2 or ZERO (has to be added normally)***

- Ideally, the `enthu = 1` will be for a person with the following stats:

```
Hall: 12
Practice_hours (ph): 18
Posts_shared (ps): 10
Bulla_hours (bh): 10
Classes_missed (cm): 0
Relationship_status (rs): SINGLE_AND_STUD
```

Now, you know how to judge the enthu of the people, your task is to fill the enthu column in the `galaxy_data.csv` file. I could've made this easy, but being practical, I deleted some random entries from the file (assume, some students were not surveyed because they were sleeping or in classes). 

### Thus, the code does the following:

- Reads the `galaxy_data.csv` file into the dataframe, or you may use the `csv` module of python.
- Fixes the missing entries, for this:
  - Practice_hours (ph): Mean of datas of the same hall.
  - Posts_shared (ps): Median of datas of the same hall.
  - Bulla_hours (bh): Median of datas of the same hall.
  - Classes_missed (cm): Mean of datas of the same hall.
  - Relationship_status (rs): SINGLE_AND_STUD (for hall 5, this would be COMMITTED_INSIDE_CAMPUS).
- Calculates the **enthu** factor for each of the entry (person), note that it could be negative also, but _cannot_ exceed 1.
- Exports a new `.csv` file in the same directory with the **enthu** of the people.
- Outputs on `stdout`, as per our prediction, the winning hall, which would be the one which has the ***highest average enthu*** of the hall residents.
