$(document).ready(function () {
  let url = $("#search");
  $("#search, #product").autocomplete({
    source: $("#search").attr("data-url"),
  });
});

// if (document.getElementById("remove-but")) {
//   $(".remove-but")
//     .append(`<form data-id="button" action="{% url 'favorite_delete' substitute.id %}" method="POST"
//     class="remove-button">
//     {% csrf_token %}
//     <button class="delete-button" name="button-save" type="submit">
//       <i id="save" class="far fa-save" aria-hidden="true"></i> Supprimer
//       des favoris
//     </button>
//   </form>

// `);
//   if (document.getElementById("save-but")) {
//     $(".save-but")
//       .append(`<form data-id="button" action="{% url 'favorite' substitute.id %}" method="POST" class="add-button">
//       {% csrf_token %}
//       <button class="save-button" name="button-save" type="submit">
//         <i id="save" class="far fa-save" aria-hidden="true"></i>
//         Sauvegarder
//       </button>
//     </form>
// `);
//   }
// }
// $("button").click(function (event) {
//   $.ajax({
//     data: {
//       id: $(this).data("id"),
//     },
//     type: "POST",
//     url: "/",
//   }).success(function (data) {
//     if (data.response == "save-but") {
//       $("#remove-but")
//         .replaceWith(`<form data-id="button" action="{% url 'favorite_delete' substitute.id %}" method="POST"
//         class="remove-button">
//         {% csrf_token %}
//         <button class="delete-button" name="button-save" type="submit">
//           <i id="save" class="far fa-save" aria-hidden="true"></i> Supprimer
//           des favoris
//         </button>
//       </form>

// `);
//     }
//     if (data.response == "remove-but") {
//       $(".add-button")
//         .replaceWith(`            <form data-id="button" action="{% url 'favorite' substitute.id %}" method="POST" class="add-button">
//         {% csrf_token %}
//         <button class="save-button" name="button-save" type="submit">
//           <i id="save" class="far fa-save" aria-hidden="true"></i>
//           Sauvegarder
//         </button>
//       </form>

// `);
//     }
//     console.log("ok");
//   }),
//     event.preventDefault();
// });

// $(document).ready(function () {
//   $("button").on("click", function (event) {
//     let buttonId = $(this).data("data-id");
//     let data = {
//       id: buttonId,
//     };
//     let url = "/";
//     $.ajax("POST", url, data, function () {
//       console.log("Appel fait !");
//     })
//       .success(function (data) {
//         if (data.response == "added") {
//           $(this).removeClass("add-button");
//           $(this).addClass("remove-button");
//         }
//         if (data.response == "removed") {
//           $(this).addClass("add-button");
//           $(this).removeClass("remove-button");
//         }
//       })
//       .fail(function () {
//         console.log("Le produit n'a pas pu être enregistré.");
//       });
//   });
//   event.preventDefault();
// });
