FROM python:3.7-stretch #DONE

RUN pip install kafka-python pymongo    #DONE

RUN mkdir /spellchecker
WORKDIR /html_extractor

COPY dao dao
COPY kafka_interface kafka_interface
COPY extractor extractor
COPY generateparseorders.py generateparseorders.py

COPY main.py main.py    #DONE

ENV KAFKA_BOOTSTRAP_SERVERS kafka:9092 #DONE
ENV KAFKA_NEW_WORDLIST_TOPIC new_wordlist
ENV KAFKA_NEW_WORDLIST_GROUP_ID words_by_length_updater

ENV MONGODB_HOST mongo #DONE
ENV MONGODB_DB default #DONE
ENV MONGODB_WORDS_BY_LENGTH_COLLECTION words_by_length #DONE

ENV MONGODB_USERNAME genericparser
ENV MONGODB_PASSWORD genericparser

ENV DEBUG true

CMD ["python3", "-u", "main.py"] #DONE