![NBA](https://github.com/Alfon22A/Mid-Boot-Camp-Project/blob/master/Slides/Images/NBALogo.png)![MVP](https://github.com/Alfon22A/Mid-Boot-Camp-Project/blob/master/Slides/Images/MVPTrophy.png)

# NBA MVPs Analysis (2000-2022)

Analysis: Alfonso Muñoz Alonso

[Tableau Presentation](https://public.tableau.com/views/NBA-MVPs-Analysis/Intro?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

## Introduction

In this project, we analyze the stats of players that received at least a vote towards the NBA MVP Regular Season Award from 2000 to 2022.

We will try to answer some questions related to the Dataset and find out if stats are as important as they seem in order to crown the winner.

We will also test some models to predict a future winner based on stats.

## Questions

- Which stat is the most influential towards winning the MVP?
- Are stats the only thing that matters?
- Is it possible to create a model that predicts the MVP?

## Info

- Points: awarded by making field goals (two or three points) or free throws (one point).
- Rebounds: awarded to a player who retrieves the ball after a missed field goal or free throw. 
- Assists: awarded to a player who passes the ball to a teammate in a way that leads directly to a score by field goal.
- Steals: awarded when a defensive player legally causes a turnover by their positive, aggressive action(s).
- Blocks: awarded when a defensive player legally deflects a field goal attempt from an offensive player to prevent a score.
- Stats: all previous awards combined.
- MVP: Most Valuable Player.
- Rank: MVP Voting standing.
- Share: percentage of the total votes obtained by a player.
- Win Shares: an estimate of the number of wins contributed by a player.
- Voter fatigue: phenomenon where a player is less likely to be voted MVP after winning the trophy the previous year(s).

## Data

- NBA MVP Voting from 2000 to 2022.

## Sources

- Basketball-Reference (Datasets)
- NBA (MVPs)
- Wikipedia (Definitions)

## Conclusions

- Which stat is the most important towards winning the MVP?
	- Points/M: 6 MVPs, ranking first on average.
	- Rebounds/M: 4 MVPs, ranking first on average.
	- Assists/M: 2 MVPs, ranking first on average.

- Are stats the only thing that matters?
	- Stats/M: 12 MVPs, ranking first on average.
	- Win Shares/48: 15 MVPs, ranking first on average.

- Is it possible to create a model that predicts the MVP?
	- No tested model was good enough.
	- Best tested model: Logistic Regression for Top 5.

## Next steps

- Include more data.
- Factor Stats and Win Shares coefficients.
- Measure Team Win percentage.
- Take voter fatigue into account.