$(document).ready(function() {
	$('.salonsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  infinite: true,
	  prevArrow: $('.salons .leftArrow'),
	  nextArrow: $('.salons .rightArrow'),
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});
	$('.servicesSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.services .leftArrow'),
	  nextArrow: $('.services .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.mastersSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.masters .leftArrow'),
	  nextArrow: $('.masters .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.reviewsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.reviews .leftArrow'),
	  nextArrow: $('.reviews .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	// menu
	$('.header__mobMenu').click(function() {
		$('#mobMenu').show()
	})
	$('.mobMenuClose').click(function() {
		$('#mobMenu').hide()
	})

	function getSlots(master_id, selected_day) {
		const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

		function csrfSafeMethod(method) {
			// these HTTP methods do not require CSRF protection
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
	
		$.ajaxSetup({
			beforeSend: function (xhr, settings) {
				// if not safe, set csrftoken
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});

		$.ajax({
			type: "POST",
			url: "./slots",
			data: {
				"master_id": master_id,
				"selected_day": selected_day,
			},
			success: function (response) {
				let slotsHTML = ``;
				for (let slot in response) {
					console.log(response[slot])
					slotsHTML += `
						<button data-time="${response[slot]['time']}" class="time__elems_btn" id="slots_${response[slot]['id']}">${response[slot]['time']}</button>
					`;
				}
				$('#slots').html(slotsHTML);
			},
			failure: function (data) {
				console.log("failure");
				console.log(data);
			},
		});
	}

	new AirDatepicker('#datepickerHere', {
		onSelect({formattedDate}) {
			const [day, month, year] = formattedDate.split('.');
			const date = `${year}-${month}-${day}`;

			$('#selected_day').val(date);
			const selected_master = $('#selected_master').val();
			if (selected_master) {
				getSlots(selected_master, date);
			}
		}
	});

	var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	  acc[i].addEventListener("click", function(e) {
	  	e.preventDefault()
	    this.classList.toggle("active");
	    var panel = $(this).next()
	    panel.hasClass('active') ?  
	    	 panel.removeClass('active')
	    	: 
	    	 panel.addClass('active')
	  });
	}

	function getMasters(studio_id, service_id) {
		const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

		function csrfSafeMethod(method) {
			// these HTTP methods do not require CSRF protection
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
	
		$.ajaxSetup({
			beforeSend: function (xhr, settings) {
				// if not safe, set csrftoken
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});

		$.ajax({
			type: "POST",
			url: "./masters",
			data: {
				"studio_id": studio_id,
				"service_id": service_id,
			},
			success: function (response) {
				let mastersHTML = `
						<div class="accordion__block fic">
							<div class="accordion__block_elems fic">
								<img src="img/masters/avatar/all.svg" alt="avatar" class="accordion__block_img">
								<div class="accordion__block_master">Любой мастер</div>
							</div>
						</div>
					`;
				for (let master in response) {
					mastersHTML += `
						<div class="accordion__block fic" id="master_${response[master]['id']}" data-type="master">
							<div class="accordion__block_elems fic">
								<img src="{% static 'img/masters/avatar/pushkinskaya/1.svg' %}" alt="avatar" class="accordion__block_img">
								<div class="accordion__block_master">${response[master]['name']}</div>
							</div>
							<div class="accordion__block_prof">${response[master]['prof']}</div>
						</div>
					`;
				}
				$('#masters').html(mastersHTML);
			},
			failure: function (data) {
				console.log("failure");
				console.log(data);
			},
		});
	}



	$(document).on('click', '.accordion__block', function(e) {
		let thisName,thisAddress;

		thisName = $(this).find('> .accordion__block_intro').text();
		thisAddress = $(this).find('> .accordion__block_address').text();
		thisId = $(this).attr('id');
		thisType = $(this).attr('data-type');
		console.log(thisId)

		if (thisType === 'studio') {
			const id = thisId.slice(7);
			$('#selected_studio').val(id);
			const selected_service = $('#selected_service').val();

			if (selected_service) {
				getMasters(id, selected_service);
			}

			// const masters = $('*[data-type="masters"]').each(function(index) {
			// 	$(this).hide();
			// });

			// $(`#masters_${id}[data-type="masters"]`).show();
		}

		if (thisType === 'master') {
			const id = thisId.slice(7);
			$('#selected_master').val(id);
			const selected_day = $('#selected_day').val();
			if (selected_day) {
				getSlots(id, selected_day);
			}
		}
	
		$(this).parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		setTimeout(() => {
			$(this).parent().parent().find('> button.active').click()
		}, 200)
		
		// $(this).parent().addClass('hide')

		// console.log($(this).parent().parent().find('.panel').hasClass('selected'))
		
		// $(this).parent().parent().find('.panel').addClass('selected')
	})


	$('.accordion__block_item').click(function(e) {
		let thisName,thisAddress;
		thisName = $(this).find('> .accordion__block_item_intro').text()
		thisAddress = $(this).find('> .accordion__block_item_address').text()

		thisId = $(this).attr('id');
		thisType = $(this).attr('data-type');

		if (thisType === 'service') {
			const id = thisId.slice(8);
			$('#selected_service').val(id);
			const selected_studio = $('#selected_studio').val();

			if (selected_service) {
				getMasters(selected_studio, id);
			}

			// const masters = $('*[data-type="masters"]').each(function(index) {
			// 	$(this).hide();
			// });

			// $(`#masters_${id}[data-type="masters"]`).show();
		}

		$(this).parent().parent().parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		// $(this).parent().parent().parent().parent().find('> button.active').click()
		// $(this).parent().parent().parent().addClass('hide')
		setTimeout(() => {
			$(this).parent().parent().parent().parent().find('> button.active').click()
		}, 200)
	})



	// 	console.log($('.service__masters > .panel').attr('data-masters'))
	// if($('.service__salons .accordion.selected').text() === "BeautyCity Пушкинская  ул. Пушкинская, д. 78А") {
	// }


	$(document).on('click', '.service__masters .accordion__block', function(e) {
		let clone = $(this).clone()
		console.log(clone)
		$(this).parent().parent().find('> button.active').html(clone)
	})

	// $('.accordion__block_item').click(function(e) {
	// 	const thisName = $(this).find('.accordion__block_item_intro').text()
	// 	const thisAddress = $(this).find('.accordion__block_item_address').text()
	// 	console.log($(this).parent().parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().find('button.active').addClass('selected').text(thisName + '  ' +thisAddress)
	// })



	// $('.accordion__block_item').click(function(e) {
	// 	const thisChildName = $(this).text()
	// 	console.log(thisChildName)
	// 	console.log($(this).parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().parent().find('button.active').addClass('selected').text(thisChildName)

	// })
	// $('.accordion.selected').click(function() {
	// 	$(this).parent().find('.panel').hasClass('selected') ? 
	// 	 $(this).parent().find('.panel').removeClass('selected')
	// 		:
	// 	$(this).parent().find('.panel').addClass('selected')
	// })


	//popup
	$('.header__block_auth').click(function(e) {
		e.preventDefault()
		$('#authModal').arcticmodal();
		// $('#confirmModal').arcticmodal();

	})

	$('.rewiewPopupOpen').click(function(e) {
		e.preventDefault()
		$('#reviewModal').arcticmodal();
	})
	$('.payPopupOpen').click(function(e) {
		e.preventDefault()
		$('#paymentModal').arcticmodal();
	})
	$('.tipsPopupOpen').click(function(e) {
		e.preventDefault()
		$('#tipsModal').arcticmodal();
	})
	
	$('.authPopup__form').submit(function() {
		$('#confirmModal').arcticmodal();
		return false
	})

	//service
	// $('.time__items .time__elems_elem .time__elems_btn').click(function(e) {
	// 	e.preventDefault()
	// 	$('.time__elems_btn').removeClass('active')
	// 	$(this).addClass('active')
	// 	// $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
	// })
	$(document).on('click', '.time__items .time__elems_elem .time__elems_btn', function(e) {
		e.preventDefault()
		$('.time__elems_btn').removeClass('active')
		$(this).addClass('active')
		thisId = $(this).attr('id');
		thisTime = $(this).attr('data-time');
		$('#selected_time').val(thisTime);
		// $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
	})

	$(document).on('click', '.servicePage', function() {
		if($('.time__items .time__elems_elem .time__elems_btn').hasClass('active') && $('.service__form_block > button').hasClass('selected')) {
			$('.time__btns_next').addClass('active')
		}
	})

	$(document).on('click', '.time__btns_next', function() {
		console.log($('#selected_service').val())
		console.log($('#selected_studio').val())
		console.log($('#selected_master').val())
		console.log($('#selected_day').val())
		console.log($('#selected_time').val())
		const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

		function csrfSafeMethod(method) {
			// these HTTP methods do not require CSRF protection
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
	
		$.ajaxSetup({
			beforeSend: function (xhr, settings) {
				// if not safe, set csrftoken
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});

		$.ajax({
			type: "POST",
			url: "./order",
			data: {
				"studio_id": $('#selected_studio').val(),
				"service_id": $('#selected_service').val(),
				"master_id": $('#selected_master').val(),
				"selected_day": $('#selected_day').val(),
				'selected_slot': $('#selected_time').val()
			},
			success: function (response) {
				console.log("success");
				console.log(response);
			},
			failure: function (data) {
				console.log("failure");
				console.log(data);
			},
		});
	})
})