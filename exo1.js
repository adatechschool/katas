function A(x) {
  function B(y) {
    function C(z) {
      function D(f) {
        console.log(x + y + z + f);
      }
      D("chien")
    } 
    C("un ");
  }
  B("a ");
}
A("Hana ");
