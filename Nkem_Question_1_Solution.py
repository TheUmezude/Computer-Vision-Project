from collections import Counter
import json
import cv2
import numpy as np
import random


# Functions Start Here ---------------------------------------------------------------------------
def unique_shape_no(sama_json):
    # Load json and take out unique shapes
    my_set = set()
    
    with open(json_file, mode = 'r', encoding = 'utf-8') as myfile:
        contents = json.load(myfile)
        
    for items in range(0, len(contents)):
        for index in range(0, len(contents[items]['taggable image'])):
            my_set.add(contents[items]['taggable image'][index]['type'])
    
    return(len(my_set))



def frequency_of_shape(sama_json):
    # Load json and take out unique shapes
    shape_set = set()
    shape_dict = {}
    
    with open(json_file, mode = 'r', encoding = 'utf-8') as myfile:
        contents = json.load(myfile)
        
    for items in range(0, len(contents)):
        for index in range(0, len(contents[items]['taggable image'])):
            shape_set.add(contents[items]['taggable image'][index]['type'])
    
    
    
    # Initialize the frequency of the shapes to 0, first - in a dictionary
    for items in shape_set:
        shape_dict[items] = 0
    
    # Update the frequency in the dictionary
    for items in range(0, len(contents)):
        for index in range(0, len(contents[items]['taggable image'])):
            for shape in shape_set:
                if contents[items]['taggable image'][index]['type'] == shape:
                    shape_dict[shape] += 1
                    
    return (shape_dict)



def shape_label_gen(sama_json):
    # Load json and take out unique shapes
    shape_set = set()
    shape_dict = {}
    shape_label_dict = {}
    label_set = set()
    
    with open(json_file, mode = 'r', encoding = 'utf-8') as myfile:
        contents = json.load(myfile)
        
    for items in range(0, len(contents)):
        for index in range(0, len(contents[items]['taggable image'])):
            shape_set.add(contents[items]['taggable image'][index]['type'])
    
    
    # Make a set of all the labels for the different shapes
    shape_set_label = set()
        
    for shape in shape_set:
        shape_label_dict[shape] = []
            
    
    for items in range(0, len(contents)):
        for index in range(0, len(contents[items]['taggable image'])):
            for shape in shape_set:
                if contents[items]['taggable image'][index]['type'] == shape:
                    shape_label_dict[shape].append(contents[items]['taggable image'][0]['tags']['label'])
                
    #return (shape_label_dict)
    dist_dict = {}     
    
    for items in shape_label_dict.keys():
        dist_dict[items] = Counter(shape_label_dict[items])
        
    return (dist_dict)
        
    

def generate_image_shape(sama_json):
    # Make empty black image
    image=np.zeros((2160,3840,3),np.uint8)
    length = 0
    
    with open(json_file, mode = 'r', encoding = 'utf-8') as myfile:
        contents = json.load(myfile)
    
    
    # Generating first image
    for items in range(0, len(contents)):
        for index in range(0, len(contents[items]['taggable image'])):
            # Drawing line images
            if contents[items]['taggable image'][index]['type'] == 'line':
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(255,255,255),5)
                
             
            # Drawing rectangle images
            elif contents[items]['taggable image'][index]['type'] == 'rect':
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (0,0,255),5)
                
                
            # Drawing polygon images
            elif contents[items]['taggable image'][index]['type'] == 'polygon':
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)
                cv2.polylines(image,[pts], True, (0,255,0),5)
                
                
    # Save the image
    cv2.imwrite("result1.png",image)
    
    return ("The generated image has been saved as 'result1.png'.")
    
    

def generate_image_label(sama_json):
    # Make empty black image
    image=np.zeros((2160,3840,3),np.uint8)
    length = 0
    
    with open(json_file, mode = 'r', encoding = 'utf-8') as myfile:
        contents = json.load(myfile)
    
    
    # Generating second image
    for items in range(0, len(contents)):
        for index in range(0, len(contents[items]['taggable image'])):
            # Drawing line images
            if (contents[items]['taggable image'][index]['type'] == 'line') and (contents[items]['taggable image'][index]['tags']['label'] == 'car'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(255,255,255),5)
                
        
            elif (contents[items]['taggable image'][index]['type'] == 'line') and (contents[items]['taggable image'][index]['tags']['label'] == 'van'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(0,255,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'line') and (contents[items]['taggable image'][index]['tags']['label'] == 'other'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(255,0,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'line') and (contents[items]['taggable image'][index]['tags']['label'] == 'bus'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(255,255,0),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'line') and (contents[items]['taggable image'][index]['tags']['label'] == 'truck'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(0,0,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'line') and (contents[items]['taggable image'][index]['tags']['label'] == 'occlusion'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(0,255,0),5)
 
            elif (contents[items]['taggable image'][index]['type'] == 'line') and (contents[items]['taggable image'][index]['tags']['label'] == 'middle line'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.line(image,(coordinates[0][0],coordinates[0][1]),(coordinates[1][0],coordinates[1][1]),(255,0,0),5)
                
            
            # Drawing rect images
            elif (contents[items]['taggable image'][index]['type'] == 'rect') and (contents[items]['taggable image'][index]['tags']['label'] == 'car'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (255,255,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'rect') and (contents[items]['taggable image'][index]['tags']['label'] == 'van'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (0,255,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'rect') and (contents[items]['taggable image'][index]['tags']['label'] == 'other'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (255,0,255),5)
    
            elif (contents[items]['taggable image'][index]['type'] == 'rect') and (contents[items]['taggable image'][index]['tags']['label'] == 'bus'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (255,255,0),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'rect') and (contents[items]['taggable image'][index]['tags']['label'] == 'truck'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (0,0,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'rect') and (contents[items]['taggable image'][index]['tags']['label'] == 'occlusion'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (0,255,0),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'rect') and (contents[items]['taggable image'][index]['tags']['label'] == 'middle line'):
                coordinates = contents[items]['taggable image'][index]['points']
                cv2.rectangle(image, (coordinates[0][0],coordinates[0][1]),(coordinates[3][0],coordinates[3][1]), (255,0,0),5)
                
            
            # For Polygon images
            elif (contents[items]['taggable image'][index]['type'] == 'polygon') and (contents[items]['taggable image'][index]['tags']['label'] == 'car'):
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)        
                cv2.polylines(image,[pts], True, (255,255,255),5)
          
            elif (contents[items]['taggable image'][index]['type'] == 'polygon') and (contents[items]['taggable image'][index]['tags']['label'] == 'van'):
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)    
                cv2.polylines(image,[pts], True, (0,255,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'polygon') and (contents[items]['taggable image'][index]['tags']['label'] == 'other'):
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)   
                cv2.polylines(image,[pts], True, (255,0,255),5)
                    
            elif (contents[items]['taggable image'][index]['type'] == 'polygon') and (contents[items]['taggable image'][index]['tags']['label'] == 'bus'):
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)      
                cv2.polylines(image,[pts], True, (255,255,0),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'polygon') and (contents[items]['taggable image'][index]['tags']['label'] == 'truck'):
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)      
                cv2.polylines(image,[pts], True, (0,0,255),5)
        
            elif (contents[items]['taggable image'][index]['type'] == 'polygon') and (contents[items]['taggable image'][index]['tags']['label'] == 'occlusion'):
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)  
                cv2.polylines(image,[pts], True, (0,255,0),5)
           
            elif (contents[items]['taggable image'][index]['type'] == 'polygon') and (contents[items]['taggable image'][index]['tags']['label'] == 'middle line'):
                coordinates = contents[items]['taggable image'][index]['points']
                pts = np.array(coordinates, np.int32)
                cv2.polylines(image,[pts], True, (255,0,0),5)
    
    
    
    
    # Save
    cv2.imwrite("result2.png",image)
    
    return ("The generated image has been saved as 'result2.png'.")
    
    
    
    
    
# Functions End Here --------------------------------------------------------------------------------------------------

    
    
json_file = input("Please enter the file path for the 'json' document you wish to load: ")
print("\n\n")

print("Please select what you would like to do:")
print("1. Get number of unique shape types.")
print("2. Get the frequency of each shape type.")
print("3. Get the frequency of the labels associated with the unique shape types.")
print("4. Generate an image where color is based on shape type (image would be saved to your PC as 'result1.png')")
print("5. Generate an image where color is based on annotation label (image would be saved to your PC as 'result2.png').")

selected_option = input()
selected_option = int(selected_option)

if selected_option == 1:
    print("\n")
    print(f"The number of unique shape types in the '.json' file is: {unique_shape_no(json_file)}")
    
elif selected_option == 2:      
    print("\n")
    print(f"The frequency of occurrence of each unique shape type is: {frequency_of_shape(json_file)}")
    
elif selected_option == 3:
    print("\n")
    print(f"The frequency of all labels associated with the unique shape types are counted as: {shape_label_gen(json_file)}")
    
elif selected_option == 4:
    print("\n")
    print(generate_image_shape(json_file))
    
elif selected_option == 5:
    print("\n")
    print(generate_image_label(json_file))
    
else:
    print("Please you would have to select a valid option.")
    

