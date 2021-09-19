# ## Write/Append the current venue's data into the file
                    # with open('single_venue_strategy_results.csv', 'a+') as f:
                    #     writer = csv.writer(f)

                    #     # check if the file is empty: if NO, write newline char, if YES do nothing,
                    #     f.seek(0) # Move read cursor to the start of file
                    #     data = f.read(10)
                    #     if len(data) > 0:
                    #         f.write("\n")
                    #     else:
                    #         writer.writerow(['venue_id','num_races',\
                    #                         'Stra1_1','Stra1_2','Stra1_3','Stra1_4','Stra1_5','Stra1_6',\
                    #                         'Stra2_1','Stra2_2','Stra2_3','Stra2_4','Stra2_5','Stra2_6',\
                    #                         'Stra3_1','Stra3_2','Stra3_3','Stra3_4','Stra3_5','Stra3_6',\
                    #                         'Stra4_11','Stra4_12','Stra4_13','Stra4_14','Stra4_15','Stra4_21','Stra4_22','Stra4_23','Stra4_24','Stra4_25','Stra4_31','Stra4_32','Stra4_33','Stra4_34','Stra4_35','Stra4_41','Stra4_42','Stra4_43','Stra4_44','Stra4_45','Stra4_51','Stra4_52','Stra4_53','Stra4_54','Stra4_55','Stra4_61','Stra4_62','Stra4_63','Stra4_64','Stra4_65',\
                    #                         'Stra5_11','Stra5_12','Stra5_13','Stra5_14','Stra5_15','Stra5_21','Stra5_22','Stra5_23','Stra5_24','Stra5_25','Stra5_31','Stra5_32','Stra5_33','Stra5_34','Stra5_35','Stra5_41','Stra5_42','Stra5_43','Stra5_44','Stra5_45','Stra5_51','Stra5_52','Stra5_53','Stra5_54','Stra5_55','Stra5_61','Stra5_62','Stra5_63','Stra5_64','Stra5_65'])    
                    #     writer.writerow(merged_stras)