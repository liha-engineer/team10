$(document).ready(function () {
  listening();
});

function listening() {
  $.ajax({
    type: "GET",
    url: "/UserList/call",
    data: {},
    success: function (response) {
      let rows = response["user_call"];
      for (let i = 0; i < rows.length; i++) {
        let name = rows[i]["name"];
        let img = rows[i]["img"];
        let comment = rows[i]["comment"];
        let id = rows[i]["id"];

        let temp_html = ` <div class="card">
                                    <div>
                                        <img src="${img}" class="profile"/>
                                    </div>
                                    <div class="user-info">
                                        <h2 id="${id}">${id}<h2>
                                        <h2>${name}</h2>
                                        <div class="comment">
                                            ${comment}
                                        </div>
                                        <div class="btn">
                                           <button type="button" class="bookmk" onclick="throw_favor_id('${id}')" style=cursor:pointer;>⭐bookmark</button>
                                        </div>
                                    </div>
                                   </div> `;

        $("#user-card").append(temp_html);
      }
    },
  });
}

function throw_favor_id(val) {
  alert(val);
  $.ajax({
    type: "POST",
    url: "/UserList/throw",
    data: { val_give: val },
    success: function (response) {},
  });
}
