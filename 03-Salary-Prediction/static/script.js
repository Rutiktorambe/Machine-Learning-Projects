
// Function to show Tier 2 and Tier 3 fields based on Metro City selection
function showTierFields() {
    var metroCity = document.getElementById('metro_city').value;
    var tierFields = document.getElementById('tier_fields');

    if (metroCity == '1') {
        // Tier 1 city, hide Tier 2 and Tier 3 fields
        tierFields.style.display = 'none';
    } else {
        // Tier 2 or Tier 3 city, show Tier 2 and Tier 3 fields
        tierFields.style.display = 'block';
    }
}

