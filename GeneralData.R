generaldata <- function(){
  
  channel_ID <- ""
  metrics <- c("views","likes","dislikes","comments","shares","subscribersGained","subscribersLost")
  filters <- NULL
  
  #Extrayendo datos diarios
  dimension <- "day"
  initial_date <- "2017-01-01"
  final_date <- "2017-12-12"
  daily_data <- yt_analytics(channel_ID, start.date = initial_date, end.date = final_date,metrics = metrics, dimensions = dimension, filters = filters)
  
  #Extrayendo datos mensuales
  dimension <- "month"
  initial_date <- "2017-01-01"
  final_date <- "2017-12-01"
  monthly_data <- yt_analytics(channel_ID, start.date = initial_date, end.date = final_date,metrics = metrics, dimensions = dimension, filters = filters)
  row.names(monthly_data) <- month.name
  monthly_data <- monthly_data[,2:ncol(monthly_data)]
  
  # 1. Generando totales de métricas generales
  print(colSums(monthly_data[,-1]))
  
  #2. Graficando datos diarios
  
   #Generando gráficas de "spikes" views (ggplot2 & gridExtra required)
  p1 <- qplot(x = day, y = views, data = daily_data, geom = "line", xlab = "Dias", ylab = "Views")
  print(p1)
  
   #Generando gráficas de "spikes" likes & dislikes
  p2 <- qplot(x = day, y = likes, data = daily_data, geom = "line", xlab = "Dias", ylab = "Likes")
  p3 <- qplot(x = day, y = dislikes, data = daily_data, geom = "line", xlab = "Dias", ylab = "Dislikes")
  grid.arrange(p2,p3)
  
   #Generando gráficas de subscribers
  p4 <- qplot(x = day, y = subscribersGained, data = daily_data, geom = "line", xlab = "Dias", ylab = "Subscriptores Ganados")
  p5 <- qplot(x = day, y = subscribersLost, data = daily_data, geom = "line", xlab = "Dias", ylab = "Subscriptores Perdidos")
  grid.arrange(p4,p5)
  
  #3. Generando tablas de datos mensuales.
  
   #Creando columnas para los porcentajes.
  d1 <- mutate_all(monthly_data, funs(./sum(.)*100))
  colnames(d1) <- c("P.Views","P.Likes", "P.Dislikes", "P.Comments", "P.Shares", "P.Subscriptores Gained", "P.Subscriptores Lost")
  monthly_data <- bind_cols(monthly_data,d1)
  monthly_data <- mutate(monthly_data, Ganancia_vs_Perdida = subscribersGained/subscribersLost)
  rownames(monthly_data) <- month.name
  
  return(list(daily_data,monthly_data))

}