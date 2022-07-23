$(document).ready(function(){
    $(".navbar-toggler").click(function(){
        $(".collapse navbar-collapse").toggleClass("mobile-menu");
    });
  });

//   To get the value of a theme from localStorage
  let theme = localStorage.getItem('theme')

  if(theme == null){
      setTheme('light')
  }else{
      setTheme(theme)
  }
  
  let themeDots = document.getElementsByClassName('theme-dots')
  
  
  for (var i=0; themeDots.length > i; i++){
      themeDots[i].addEventListener('click', function(){
          let mode = this.dataset.mode
          console.log('Option clicked:', mode)
          setTheme(mode)
      })
  }
  
  function setTheme(mode){
      if(mode == 'light'){
          document.getElementById('theme-style').href = 'CSS/Style.css'
      }
  
      if(mode == 'cyan'){
          document.getElementById('theme-style').href = 'CSS/cyan.css'
      }
  
      if(mode == 'brown'){
          document.getElementById('theme-style').href = 'CSS/brown.css'
      }
  
      if(mode == 'gray'){
          document.getElementById('theme-style').href = 'CSS/gray.css'
      }
      if(mode == 'dark'){
        document.getElementById('theme-style').href = 'CSS/dark.css'
    }
  
      localStorage.setItem('theme', mode)
  }