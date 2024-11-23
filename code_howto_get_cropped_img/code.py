 #save cropped image of the player
    for track_id, player in tracks['players'][0].items():
        bbox=player['bbox']
        frame=video_frames[0]
    
    # corp bbox from the frame
        cropped_image =frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

    #save the cropped image 
        cv2.imwrite(f'output_videos/cropped_image.jpg',cropped_image)
        break


## copy this code into the main and then run it before running the color_assignment_analysis  