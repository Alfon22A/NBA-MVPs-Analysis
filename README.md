![NBA](https://github.com/Alfon22A/Mid-Boot-Camp-Project/blob/master/Slides/Images/NBALogo.png)![MVP](https://github.com/Alfon22A/Mid-Boot-Camp-Project/blob/master/Slides/Images/MVPTrophy.png)

# NBA MVPs Analysis (2000-2022)

[Tableau Presentation](https://public.tableau.com/views/NBA-MVPs-Analysis/Intro?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

## Introduction

In this project, we analize the stats of players that recieved at least a vote towards the NBA MVP Regular Season Award from 2000 to 2022.

We will try to answer some questions related to the Dataset and find out if stats are as important as they seem in order to crown the winner.

We will also test some models to predict a future winner based on stats.

## Questions
- Which stat is the most important towards winning the MVP?
- Are stats the only thing that matters?
- Is it possible to create a model that predicts the MVP?

## Info
- Points: awarded by making field goals (two or three points) or free throws (one point). [Wikipedia](https://en.wikipedia.org/wiki/Point_(basketball))
- Rebounds: awarded to a player who retrieves the ball after a missed field goal or free throw. [Wikipedia](https://en.wikipedia.org/wiki/Rebound_(basketball))
- Assists: awarded to a player who passes the ball to a teammate in a way that leads directly to a score by field goal. [Wikipedia](https://en.wikipedia.org/wiki/Assist_(basketball))
- Steals: awarded when a defensive player legally causes a turnover by their positive, aggressive action(s). [Wikipedia](https://en.wikipedia.org/wiki/Steal_(basketball))
- Blocks: awarded when defensive player legally deflects a field goal attempt from an offensive player to prevent a score. [Wikipedia](https://en.wikipedia.org/wiki/Block_(basketball))
- Stats: all previous awards combined.
- MVP: Most Valuable Player [Wikipedia](https://en.wikipedia.org/wiki/NBA_Most_Valuable_Player_Award)
- Rank: MVP Votings order.
- Share: percentage of the total votes obtained by a player.
- Win Shares: an estimate of the number of wins contributed by a player. [Basketball-Reference](https://www.basketball-reference.com/about/ws.html)
- Voter fatigue: phenomenon where a player is less likely to be voted MVP after winning the trophy the previous year(s).

## Data
- NBA MVPs Votings from 2000 to 2022

## Sources
- [Basketball-Reference (Datasets)](https://www.basketball-reference.com/awards/awards_2000.html)
- [NBA (MVPs)](https://www.nba.com/news/history-mvp-award-winners)
- Wikipedia (Definitions)

## Conclusions

### Which stat is the most important towards winning the MVP?
- Points/M: 6 MVPs, ranking first on average.
- Rebounds/M: 4 MVPs, ranking first on average.
- Assists/M: 2 MVPs, ranking first on average.

### Are stats the only thing that matters?
- Stats/M: 12 MVPs, ranking first on average.
- Win Shares/48: 15 MVPs, ranking first on average.

### Is it possible to create a model that predicts the MVP?
- No tested model was good enough.
- Best tested model: Logistic Regression for Top 5.

### Next steps
- Including more data.
- Factoring Stats and Win Shares coeficients.
- Including Team Win%
- Taking voter fatigue into account.