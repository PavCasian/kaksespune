// add an additional textbox if there are more translations
$(document).ready(function(){
    var counter = 1
    $(".addButton").click(function () {
      if(counter==6){
        alert ("Sorry, you've reached the number of maximum boxes. Please contact us if you want this to be increased.");
        return false;
        }  // the limit on the number of boxes

      var newTextBoxDiv = $(document.createElement('div'))
        .attr("id", 'TextBoxDiv' + counter);
      var parentDivId = $(this).closest('div').attr('id');
      // to group the words of the same language we extract the language from the div name, e.g. romanianDiv
      var langVersion = parentDivId.split('Div')[0];
      newTextBoxDiv.after().html('<input type="text" name="' + langVersion + '" id="textbox' + counter + '" value="" >');

      newTextBoxDiv.appendTo('#' + parentDivId);

      counter++;
    });

    $(".removeButton").click(function () {
        if(counter==1){
            alert("No more text boxes to remove");
            return false;
        }
        counter--;

        $("#TextBoxDiv" + counter).remove();
    });
});