
def count_batteries_by_health(present_capacities):
  healthy_dict={"healthy":0,"exchange":0,"failed":0}
  rated_capacity=120
  for i in present_capacities:
    soh=(i/rated_capacity)*100
    if soh>80 and soh<=100:
      healthy_dict["healthy"]+=1
    elif soh>62 and soh<=80:
      healthy_dict["exchange"]+=1
    elif soh<=62 and soh>=0:
      healthy_dict["failed"]+=1
  return healthy_dict


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  #Additional test case
  
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
