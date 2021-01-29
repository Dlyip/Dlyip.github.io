/* This function will create an object called
Person
 */
function Person(name, mother, spouse, child){
    this.name = name; // Name of person
    this.mother = mother; // Mother of person
    this.spouse = spouse; // Spouse of person
    // Set children variable to string
    if (this.children === undefined){
        this.children = "";
    }
    this.children += child; // Children of person
    // Function to change spouses.
    this.changeSpouse = function (name) {
        this.spouse = name;
    }
}
