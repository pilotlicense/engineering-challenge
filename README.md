# engineering-challenge
--Food Truck Engineering Challenge--

Download the latest food truck data:
```python
python food_truck_tool.py download
```
List all food trucks:
```python
python food_truck_tool.py list-trucks
```
Filter food trucks by cuisine:
```python
python food_truck_tool.py list-trucks --cuisine "Tacos"
```
Filter food trucks by facility type (e.g., Truck, Push Cart):
```python
python food_truck_tool.py list-trucks --facility-type "Truck"
```
Show food trucks open now:
```python
python food_truck_tool.py list-trucks --open-now
```
Combine filters for cuisine and facility type:
```python
python food_truck_tool.py list-trucks --cuisine "Tacos" --facility-type "Truck" --open-now
```
