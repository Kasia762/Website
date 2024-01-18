function ShowSelected(event, NavigationSelectionID) {
  // Hide the sections
  var sections = document.getElementsByClassName('page-content');
  for (var i = 0; i < sections.length; i++) {
      sections[i].classList.remove('active-section');
  }

  // Display the selected section
  var selectedSection = document.getElementById(NavigationSelectionID);
  selectedSection.classList.add('active-section');
}

function showDefaultSection() {
  // Show the home section by default
  var defaultSection = document.getElementById('home-section');
  defaultSection.classList.add('active-section');
}