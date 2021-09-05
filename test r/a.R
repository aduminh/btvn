install.packages("magrittr")
library(readxl)
library(magrittr)
library(dplyr)
library(ggplot2)

data_2014_2017 <- read_excel("C:/Users/admin/Downloads/data_2014_2017.xls"
data_2017_2019_2_ <- read_excel("C:/Users/admin/Downloads/data_2017_2019 (2).xlsx"

new_2014_2017 <- data_2014_2017 %>%
  select(Categories, `3_all_students`,`5_instructors`) %>%
  mutate(Ratio = round(`3_all_students`/`5_instructors`,2)) %>%
  select(Categories, Ratio) %>%
  rename(AcademicYear = Categories)

new_2017_2019 <- data_2017_2019_2_ %>%
  filter (school_type == "total") %>%
  select (academic_year, `4_all_undergraduate_students`, `5_all_graduate_students`, `7.3_Instructor`) %>%
  mutate(Ratio=round((`4_all_undergraduate_students`+`5_all_graduate_students`)/`7.3_Instructor`,2)) %>%
  select(academic_year, Ratio) %>%
  rename(AcademicYear = academic_year)


