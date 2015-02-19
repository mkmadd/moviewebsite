<div class="col-md-6 col-lg-4 movie-tile text-center">
    <!-- HTML below with some CSS gives a div with image background that on hover shows text overlay -->
    <div class="movie-image centered"
         style="background: url({{movie.poster_image_url}}) 0 0/220px 342px no-repeat;" 
         data-trailer-youtube-id="{{movie.trailer_youtube_id}}"
         data-toggle="modal" data-target="#trailer">
        <div class="image-text">
            <p>{{movie.storyline}}</p>
        </div>
    </div>
    <a href='/{{index}}'><h2>{{movie.title}}</h2></a>
</div>