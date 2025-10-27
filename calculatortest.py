import calculator

def test_batches(metingen:list):
    print(f"...BATCH{metingen}test!")
    for meting in metingen:
        assert meting <= 26, f"Foutmelding: {meting} is hoger dan 26"
        print(f"{meting} is goedgekeurd")

# call the test function for each batch
test_batches(calculator.batch_one)
test_batches(calculator.batch_two)
test_batches(calculator.batch_three)