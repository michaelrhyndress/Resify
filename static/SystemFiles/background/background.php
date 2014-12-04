<script src="masonry.pkgd.min.js"></script>

<style>
	* {
	-webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

body { font-family: sans-serif; margin-top: 0; margin: 0;  min-width:125%; overflow:initial;}

.masonry {
	background: #fff;
	margin: 0;
	padding:0;
}

.masonry .item {
	width:  125px;
	height: 130px;
	float: left;
	margin-bottom: 0px;
}
	@media all and (max-width: 699px){
		img{
			width:	110px;
			height: 110px;
			filter: url(filters.svg#grayscale); /* Firefox 3.5+ */
			filter: gray; /* IE6-9 */
			-webkit-filter: grayscale(1); /* Google Chrome, Safari 6+ & Opera 15+ */
		}
		.masonry .item {
			width:  110px;
			height: 115px;
			float: left;
			margin-bottom: 0px;
}
	}
	@media all and (min-width: 699px){
		img{
			width:	150px;
			height: 150px;
			filter: url(filters.svg#grayscale); /* Firefox 3.5+ */
			filter: gray; /* IE6-9 */
			-webkit-filter: grayscale(1); /* Google Chrome, Safari 6+ & Opera 15+ */
		}
		.masonry .item {
			width:  150px;
			height: 155px;
			float: left;
			margin-bottom: 0px;
		}
	}
	img:hover {
		filter: none;
		-webkit-filter: grayscale(0);
	}
}
</style>
<script>
var container = document.querySelector('#container');
var msnry = new Masonry( container, {
  // options
  columnWidth: 150,
  itemSelector: '.item'
});
</script>
<body>
<div class="masonry js-masonry"  data-masonry-options='{ "isFitWidth": true, "gutter": 6 }'>
<?php for ($i=0; $i<50; $i++){
  echo '<div class="item" ><img src="background/face.jpg" style="filter: none;
    -webkit-filter: grayscale(0);"></img></div>';
}?>
</div>
</body>