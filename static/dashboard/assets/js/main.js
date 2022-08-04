var elBtn = document.querySelector(".burger__btn");
var elBtn1 = document.querySelector(".burger-close");
var elheader = document.querySelector(".header__container");


// alert("Siuuuuu")

elBtn.addEventListener("click", function (evt) {
    elheader.classList.add("header-toggle")

	// alert("Search bardan umidni uz, bratishka!!!")
})

elBtn1.addEventListener("click", function (evt) {
    elheader.classList.remove("header-toggle")
	// alert("Qale yoqdimi?")
})


function confirm_category_delete(id){
			var r = confirm("Ushbu kategoriyani o'chirmoqchimisiz?");
			if (r == true) {
				window.location.href="/dashboard/project/delete/"+ id +"/"
			}
		}
