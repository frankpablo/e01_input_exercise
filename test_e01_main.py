def test_input_and_output(capsys, monkeypatch):

   # Create a list of input values
   inputs = iter(["Pablo", "4", "1"])
   
   # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   with monkeypatch.context() as m:
      m.setattr('builtins.input', lambda _: next(inputs))

      import e01_main  # Import the module here

      captured = capsys.readouterr()

      assert e01_main.name == "Pablo", "Tip: Did you assign the name correctly?"
      assert e01_main.num_dogs == 4, "Tip: Is the type of the value correct?"
      assert e01_main.num_cats == 1, "Tip: Is the type of the value correct?"
      assert "total_pets: 5" in captured.out, "Tip: are you able to add the values?"
