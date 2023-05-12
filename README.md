# Annual report obligations
## python version 2.7

- Create annual report obligations
- Join submitted report with obligations
- Track exceptions 
- Track reporting obligation status

# Requirements
1. Generate reporting obligations on daily basis
2. Generate historical obligations for list of entities and periods
3. Join submitted report with obligations and update obligation status.
4. Taking account slowly changing dimensions (reporting periods, entity types, changes in reporting obligation terms etc)

# Input
- Entity status and changes during entity timeline
- Entiy financial report period and it's changes
- Entity type and it's changes
- Special rules for finding reporting obligation fact based on entity type
- Different types of reporting obligations (annual, liquidation and closing reports)